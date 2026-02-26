import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Database configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "qued_india_initial")

def get_db_engine():
    """Creates and returns a SQLAlchemy engine."""
    try:
        # Create database URL
        # We need to URL encode the password to handle special characters
        password = quote_plus(DB_PASSWORD) if DB_PASSWORD else ""
        sqlalchemy_database_url = f"mysql+pymysql://{DB_USER}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        
        # Create engine
        engine = create_engine(sqlalchemy_database_url)
        return engine
    except Exception as e:
        print(f"Error creating database engine: {e}")
        return None

def import_csv_to_mysql():
    """Imports a CSV file into a MySQL table."""
    print("--- Bulk CSV Data Importer ---")
    
    # 1. Get CSV file path
    csv_file_path = input("Enter the full path to your CSV file: ").strip()
    
    # Remove quotes if the user copied as path
    if csv_file_path.startswith('"') and csv_file_path.endswith('"'):
        csv_file_path = csv_file_path[1:-1]
        
    if not os.path.isfile(csv_file_path):
        print(f"Error: File not found at {csv_file_path}")
        return

    # 2. Get table name
    table_name = input("Enter the MySQL table name to import into: ").strip()
    if not table_name:
        print("Error: Table name cannot be empty.")
        return

    # 3. Get import mode
    print("\nSelect import mode:")
    print("1. fail (Raise error if table exists)")
    print("2. replace (Drop table before inserting new values)")
    print("3. append (Insert new values to the existing table)")
    mode_choice = input("Enter choice (1/2/3) [default: append]: ").strip()
    
    if mode_choice == '1':
        if_exists = 'fail'
    elif mode_choice == '2':
        if_exists = 'replace'
    else:
        if_exists = 'append'

    print(f"\nReading CSV file: {csv_file_path}...")
    try:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(csv_file_path)
        print(f"Successfully read {len(df)} rows and {len(df.columns)} columns.")
        print(f"Columns: {', '.join(df.columns)}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Confirm before proceeding
    confirm = input(f"\nReady to import {len(df)} rows into table '{table_name}' (mode: {if_exists}). Proceed? (y/n): ").lower()
    if confirm != 'y':
        print("Import cancelled.")
        return

    print("\nConnecting to database...")
    engine = get_db_engine()
    if not engine:
        return

    try:
        print(f"Importing data into '{table_name}'...")
        # Write DataFrame to MySQL
        df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
        print(f"Success! Data imported into table '{table_name}'.")
    except ValueError as ve:
        print(f"Import Error: {ve}")
        print("Hint: If the table exists, try using 'append' or 'replace' mode.")
    except Exception as e:
        print(f"Database Error: {e}")

if __name__ == "__main__":
    import_csv_to_mysql()
