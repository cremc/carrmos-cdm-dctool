import sys
import os
from sqlalchemy import text

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine

def fix_schema():
    print("Fixing usage of sector_id -> industry_sector_id...")
    with engine.connect() as connection:
        try:
            # Check if column exists first to be safe? 
            # Or just try to rename. MySQL 8.0+ syntax
            # Note: dependent keys might be an issue.
            # MySQL often requires dropping FK first if renaming column? 
            # Let's try simple RENAME first.
            cmd = text("ALTER TABLE industry CHANGE COLUMN sector_id industry_sector_id INT;")
            connection.execute(cmd)
            connection.commit()
            print("Successfully renamed column.")
        except Exception as e:
            print(f"Error renaming column: {e}")
            # Identify if it failed because it doesn't exist (already renamed?)
            # or constraint issues.

if __name__ == "__main__":
    fix_schema()
