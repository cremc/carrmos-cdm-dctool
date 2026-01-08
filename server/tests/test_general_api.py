import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_general_domain():
    print("Testing General Domain APIs...")

    # 1. Country Group
    response = client.post("/general/country_groups/", json={"name": "SAARC", "description": "South Asian Association for Regional Cooperation"})
    assert response.status_code == 200
    group_id = response.json()["country_group_id"]
    print(f"Country Group Created: {group_id}")

    # 2. Country
    response = client.post("/general/countries/", json={
        "name": "India",
        "region": "South Asia",
        "continent": "Asia",
        "country_dialing_code": "+91"
    })
    assert response.status_code == 200
    country_id = response.json()["country_id"]
    print(f"Country Created: {country_id}")

    # 3. Country Country Group (Relationship)
    response = client.post("/general/country_groups/members/", json={
        "country_id": country_id,
        "country_group_id": group_id
    })
    assert response.status_code == 200
    rel_id = response.json()["country_country_group_id"]
    print(f"Country-Group Relationship Created: {rel_id}")

    # 4. Province/State
    response = client.post("/general/provinces/", json={
        "name": "Maharashtra",
        "country_id": country_id
    })
    assert response.status_code == 200
    province_id = response.json()["province_or_state_id"]
    print(f"Province Created: {province_id}")

    # 5. City
    response = client.post("/general/cities/", json={
        "name": "Mumbai",
        "province_or_state_id": province_id
    })
    assert response.status_code == 200
    city_id = response.json()["city_id"]
    print(f"City Created: {city_id}")

    # 6. Location
    response = client.post("/general/locations/", json={
        "location_name": "Main Office",
        "city_id": city_id,
        "province_or_state_id": province_id,
        "country_id": country_id,
        "location_type": "Office"
    })
    assert response.status_code == 200
    location_id = response.json()["location_id"]
    print(f"Location Created: {location_id}")

    # 7. Contact Details
    response = client.post("/general/contact_details/", json={
        "phone_number1": "1234567890",
        "email1": "test@example.com"
    })
    assert response.status_code == 200
    contact_id = response.json()["contact_details_id"]
    print(f"Contact Details Created: {contact_id}")

    # Cleanup
    client.delete(f"/general/contact_details/{contact_id}")
    client.delete(f"/general/locations/{location_id}")
    client.delete(f"/general/cities/{city_id}")
    client.delete(f"/general/provinces/{province_id}")
    client.delete(f"/general/country_groups/members/{rel_id}")
    client.delete(f"/general/countries/{country_id}")
    client.delete(f"/general/country_groups/{group_id}")
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_general_domain()
        print("All General Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
