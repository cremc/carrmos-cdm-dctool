import sys
import os
from sqlalchemy import inspect

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine
import app.models # Ensure models are loaded to check expected vs actual, if we want to go deeper later

def verify_tables():
    print("Verifying tables...")
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("Tables found in database:")
        for table in tables:
            print(f"- {table}")
        
        if not tables:
            print("No tables found!")
        else:
            print(f"Total tables found: {len(tables)}")
            
    except Exception as e:
        print(f"Error verifying tables: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_tables()
