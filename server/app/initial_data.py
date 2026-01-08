
import logging
import csv
import os
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import general, user
from app.core import security

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CSV_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Data_seeding.csv")
# Adjust path to find the file in root or wherever it is. 
# User said file is at: c:\Users\Atul\OneDrive\Personal\4_My_Development_Projects\1_CARRMOS\CDM_DCtool\Data_seeding.csv
# This script is at: c:\Users\Atul\OneDrive\Personal\4_My_Development_Projects\1_CARRMOS\CDM_DCtool\server\app\initial_data.py
# So relative path is ../../Data_seeding.csv
REAL_CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "Data_seeding.csv")


def parse_csv_sections(file_path):
    sections = {}
    current_section = None
    headers = None
    
    if not os.path.exists(file_path):
        logger.error(f"CSV file not found at {file_path}")
        return sections

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            
            # Check for table definition
            # Format seems to be "table:,name,..." or "table,name..."
            # Let's inspect the first cell or join row to find "table"
            first_cell = row[0].strip().lower() if row[0] else ""
            
            if 'table' in first_cell or (len(row) > 1 and 'table' in row[0].lower()):
                # It's a new table section
                # The table name might be in the second cell
                # Examples: "table:,country" or "table,province_or_state"
                table_name = row[1].strip()
                current_section = table_name
                sections[current_section] = []
                headers = None # Reset headers for next line
                logger.info(f"Found section: {current_section}")
                continue
            
            if current_section:
                if headers is None:
                    # This row contains headers
                    # Normalizing headers to strip whitespace
                    headers = [h.strip() for h in row]
                    continue
                else:
                    # Data row
                    record = {}
                    for i, value in enumerate(row):
                        if i < len(headers) and headers[i]:
                            record[headers[i]] = value.strip()
                    sections[current_section].append(record)
    
    return sections

def seed_geography(db: Session, sections):
    # Dictionary to map CSV ID to DB ID for Countries
    country_csv_id_map = {}

    # 1. Seed Countries
    if 'country' in sections:
        logger.info(f"Seeding {len(sections['country'])} countries...")
        first = True
        for row in sections['country']:
            if first:
                logger.info(f"First country keys: {row.keys()}")
                first = False

            name = row.get('name') # Lowercase n
            if not name: continue
            
            # Check if exists
            country = db.query(general.Country).filter(general.Country.name == name).first()
            if not country:
                country = general.Country(
                    name=name,
                    region=row.get('region'), # Lowercase
                    continent=row.get('continent'), # Lowercase
                    country_dialing_code=row.get('country_dialing_code')
                )
                db.add(country)
                db.commit() # Commit to get ID
                db.refresh(country)
            
            # Store mapping
            csv_id = row.get('country_id') # country_id instead of ID
            if csv_id:
                country_csv_id_map[csv_id] = country.country_id
    else:
        logger.warning("No 'country' section found in CSV")

    # 2. Seed States
    if 'province_or_state' in sections:
        logger.info(f"Seeding {len(sections['province_or_state'])} states...")
        count = 0 
        for row in sections['province_or_state']:
            name = row.get('name')
            csv_country_id = row.get('country_id')
            
            if not name or not csv_country_id: continue
            
            # Resolve Country ID
            db_country_id = country_csv_id_map.get(csv_country_id)
            if not db_country_id:
                # Fallback: maybe the country existed before and wasn't in our map (unlikely for fresh seed)
                # or CSV ID mismatch.
                # Try validation:
                # logger.warning(f"Could not find seeded country for CSV ID {csv_country_id}")
                continue
                
            # Check if state exists
            state = db.query(general.ProvinceOrState).filter(
                general.ProvinceOrState.name == name,
                general.ProvinceOrState.country_id == db_country_id
            ).first()
            
            if not state:
                state = general.ProvinceOrState(
                    name=name,
                    description=row.get('description'),
                    country_id=db_country_id
                )
                db.add(state)
                count += 1
                if count % 100 == 0:
                     db.commit() # Batch commit
        db.commit()
        logger.info("States seeding completed")
    else:
        logger.warning("No 'province_or_state' section found in CSV")

def seed_users(db: Session):
    admin_email = "dbadmin@carrmos.com"
    admin_user = db.query(user.User).filter(user.User.email == admin_email).first()
    
    if not admin_user:
        new_admin = user.User(
            email=admin_email,
            hashed_password=security.get_password_hash("password123"),
            first_name="CDM",
            last_name="Admin",
            is_active=True,
            db_role=100
        )
        db.add(new_admin)
        db.commit()
        logger.info(f"Seeded Admin User: {admin_email}")
    else:
        logger.info(f"Admin User {admin_email} already exists")

def init_db():
    db = SessionLocal()
    try:
        sections = parse_csv_sections(REAL_CSV_PATH)
        seed_geography(db, sections)
        seed_users(db)
    finally:
        db.close()

if __name__ == "__main__":
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")
