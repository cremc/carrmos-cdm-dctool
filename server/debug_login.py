
from app.database import SessionLocal
from app.models.user import User
from app.core.security import verify_password
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify():
    db = SessionLocal()
    email = "dbadmin@carrmos.com"
    password = "password123"
    
    print(f"Checking user: {email}")
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        print("[-] User NOT FOUND in database.")
    else:
        print(f"[+] User found: ID={user.users_id}, Email={user.email}")
        print(f"    Hashed Password in DB: {user.hashed_password}")
        
        is_valid = verify_password(password, user.hashed_password)
        if is_valid:
            print("[+] Password verification SUCCESS.")
        else:
            print("[-] Password verification FAILED.")
            # Debugging hash mismatch
            new_hash = pwd_context.hash(password)
            print(f"    Expected hash for '{password}' would look something like: {new_hash}")

    db.close()

if __name__ == "__main__":
    verify()
