import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_ranking_domain():
    print("Testing Ranking Domain APIs...")

    # 1. Ranking Source
    response = client.post("/ranking/sources/", json={
        "name": "QS World Ranking",
        "year_of_survey": 2025,
        "ranking_type": "Global"
    })
    assert response.status_code == 200
    source_id = response.json()["ranking_source_id"]
    print(f"Ranking Source Created: {source_id}")

    # Cleanup
    client.delete(f"/ranking/sources/{source_id}")
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_ranking_domain()
        print("All Ranking Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
