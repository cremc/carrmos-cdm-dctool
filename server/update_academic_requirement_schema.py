from sqlalchemy import create_engine, text
from app.database import SQLALCHEMY_DATABASE_URL

def add_column():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    with engine.connect() as connection:
        try:
            print("Adding 'dependency_type' column to 'milestone_academic_requirement' table...")
            connection.execute(text("ALTER TABLE milestone_academic_requirement ADD COLUMN dependency_type VARCHAR(100)"))
            print("Column added successfully.")
        except Exception as e:
            # Check if error is because column already exists
            if "Duplicate column name" in str(e):
                 print("Column 'dependency_type' already exists.")
            else:
                print(f"Error adding column: {e}")

if __name__ == "__main__":
    add_column()
