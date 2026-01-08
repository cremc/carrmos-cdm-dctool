import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_institution_domain():
    print("Testing Institution Domain APIs...")

    # 1. Institution Category
    response = client.post("/institution/categories/", json={
        "name": "University",
        "popular_name": "Varsity",
        "description": "Higher education institution"
    })
    assert response.status_code == 200
    category_id = response.json()["institution_category_id"]
    print(f"Institution Category Created: {category_id}")

    # 2. Association Accreditation Affiliation (AAA)
    response = client.post("/institution/aaa/", json={
        "name": "NAAC",
        "description": "National Assessment and Accreditation Council"
    })
    assert response.status_code == 200
    aaa_id = response.json()["aaa_id"]
    print(f"AAA Created: {aaa_id}")

    # 3. Institution
    response = client.post("/institution/institutions/", json={
        "name": "Indian Institute of Technology, Bombay",
        "short_description": "IIT Bombay",
        "popular_names": "IITB",
        "year_established": 1958,
        "url": "https://www.iitb.ac.in",
        "location": "Powai, Mumbai"
    })
    assert response.status_code == 200
    institution_id = response.json()["institution_id"]
    print(f"Institution Created: {institution_id}")

    # 4. Verify Read
    response = client.get(f"/institution/institutions/{institution_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Indian Institute of Technology, Bombay"
    print("Institution Read Verified.")

    # 5. Cleanup
    client.delete(f"/institution/institutions/{institution_id}")
    client.delete(f"/institution/aaa/{aaa_id}")
    client.delete(f"/institution/categories/{category_id}")
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_institution_domain()
        print("All Institution Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
