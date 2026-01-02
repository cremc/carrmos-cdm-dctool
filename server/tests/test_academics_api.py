import sys
import os
from fastapi.testclient import TestClient
import pytest

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
from app.database import Base, engine, SessionLocal

# Create a TestClient
client = TestClient(app)

def test_crud_academic_level():
    # 1. Create
    response = client.post(
        "/academics/academic_levels/",
        json={
            "name": "Test Level",
            "description": "A test academic level",
            "min_years_to_complete": 3,
            "average_years_to_complete": 4,
            "max_years_to_complete": 5,
            "order": 1
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Level"
    assert "academic_level_id" in data
    academic_level_id = data["academic_level_id"]

    # 2. Read
    response = client.get(f"/academics/academic_levels/{academic_level_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Level"
    assert data["description"] == "A test academic level"

    # 3. Update
    response = client.put(
        f"/academics/academic_levels/{academic_level_id}",
        json={
            "name": "Updated Test Level",
            "description": "Updated description"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Test Level"
    assert data["description"] == "Updated description"

    # 4. Delete
    response = client.delete(f"/academics/academic_levels/{academic_level_id}")
    assert response.status_code == 200
    
    # 5. Verify Delete
    response = client.get(f"/academics/academic_levels/{academic_level_id}")
    assert response.status_code == 404

def test_crud_stream():
    # Create Stream
    response = client.post(
        "/academics/streams/",
        json={
            "name": "Test Stream",
            "description": "Test Stream Description"
        }
    )
    assert response.status_code == 200
    stream_id = response.json()["stream_id"]

    # Read
    response = client.get(f"/academics/streams/{stream_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Stream"

    # Delete
    client.delete(f"/academics/streams/{stream_id}")
    assert client.get(f"/academics/streams/{stream_id}").status_code == 404

if __name__ == "__main__":
    print("Running manual tests...")
    try:
        test_crud_academic_level()
        print("AcademicEntity CRUD create/read/update/delete passed!")
        test_crud_stream()
        print("Stream CRUD create/read/delete passed!")
        print("All tests passed successfully.")
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
