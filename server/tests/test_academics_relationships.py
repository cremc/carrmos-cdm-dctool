import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_relationship_apis():
    # 1. Create Core Subject
    response = client.post(
        "/academics/core_subjects/",
        json={
            "name": "Math",
            "description": "Mathematics"
        }
    )
    assert response.status_code == 200
    core_subject_id = response.json()["core_subject_id"]
    print(f"Created Core Subject ID: {core_subject_id}")

    # 2. Create Academic Level (Prerequisite for Course)
    response = client.post(
        "/academics/academic_levels/",
        json={
            "name": "Undergraduate",
            "description": "Bachelor's Degree",
            "min_years_to_complete": 3,
            "average_years_to_complete": 4,
            "max_years_to_complete": 5,
            "order": 1
        }
    )
    assert response.status_code == 200
    academic_level_id = response.json()["academic_level_id"]

    # 3. Create Course General
    response = client.post(
        "/academics/course_generals/",
        json={
            "academic_level_id": academic_level_id,
            "name": "B.Sc Math",
            "description": "Bachelor of Science in Mathematics",
            "course_tuition_cost_inr": 50000
        }
    )
    assert response.status_code == 200
    course_general_id = response.json()["course_general_id"]
    print(f"Created Course General ID: {course_general_id}")

    # 4. Link Core Subject to Course
    response = client.post(
        "/academics/course_generals/core_subjects/",
        json={
            "course_general_id": course_general_id,
            "core_subject_id": core_subject_id
        }
    )
    assert response.status_code == 200
    relationship_id = response.json()["course_general_core_subject_id"]
    print(f"Created Relationship ID: {relationship_id}")

    # 5. Verify Link
    response = client.get(f"/academics/course_generals/{course_general_id}/core_subjects/")
    assert response.status_code == 200
    links = response.json()
    assert len(links) > 0
    assert links[0]["core_subject_id"] == core_subject_id
    print("Relationship verified.")

    # 6. Delete Link
    response = client.delete(f"/academics/course_generals/core_subjects/{relationship_id}")
    assert response.status_code == 200
    print("Relationship deleted.")

    # 7. Cleanup
    client.delete(f"/academics/course_generals/{course_general_id}")
    client.delete(f"/academics/core_subjects/{core_subject_id}")
    client.delete(f"/academics/academic_levels/{academic_level_id}")

if __name__ == "__main__":
    try:
        test_relationship_apis()
        print("All relationship tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
