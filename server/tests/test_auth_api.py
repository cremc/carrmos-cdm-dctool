import sys
import os
import secrets
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_auth_flow():
    print("Testing Authentication APIs...")

    # Generate a unique email for each run
    unique_email = f"user_{secrets.token_hex(4)}@example.com"
    password = "testpassword123"

    # 1. Signup
    print(f"1. Attempting Signup with {unique_email}...")
    signup_response = client.post("/api/users/", json={
        "email": unique_email,
        "password": password,
        "full_name": "Test User"
    })
    
    # Assert successful creation
    assert signup_response.status_code == 200, f"Signup failed: {signup_response.text}"
    user_data = signup_response.json()
    assert user_data["email"] == unique_email
    assert "id" in user_data
    print(f"Signup Successful. User ID: {user_data['id']}")

    # 2. Login
    print("2. Attempting Login...")
    login_response = client.post("/api/login/access-token", data={
        "username": unique_email,
        "password": password
    })
    
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    access_token = token_data["access_token"]
    print("Login Successful. Token received.")

    # 3. Access Protected Route (Me)
    print("3. Accessing Protected Route (/users/me)...")
    me_response = client.get("/api/users/me", headers={
        "Authorization": f"Bearer {access_token}"
    })
    
    assert me_response.status_code == 200, f"Protected route access failed: {me_response.text}"
    me_data = me_response.json()
    assert me_data["email"] == unique_email
    print("Protected Route Accessed Successfully.")

if __name__ == "__main__":
    try:
        test_auth_flow()
        print("All Authentication tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
