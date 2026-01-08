import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_requirement_domain():
    print("Testing Requirement Domain APIs...")

    # 1. Grouping Reference
    response = client.post("/requirement/grouping_references/", json={
        "Grouping_for": "Admission",
        "Milestone_type": "Academic"
    })
    assert response.status_code == 200
    group_id = response.json()["requirement_group_id"]
    print(f"Grouping Reference Created: {group_id}")

    # 2. Academic Requirement
    response = client.post("/requirement/academic_requirements/", json={
        "name": "High School Diploma",
        "dependency_type": "Mandatory",
        "requirement_group_id": group_id,
        "prerequisite_score_value_min": 85.0
    })
    assert response.status_code == 200
    acad_id = response.json()["milestone_academic_requirement_id"]
    print(f"Academic Requirement Created: {acad_id}")

    # 3. Workex Requirement
    response = client.post("/requirement/workex_requirements/", json={
        "name": "Software Engineering Intern",
        "dependency_type": "Optional",
        "prerequisite_workex_min_duration_yrs": 0.5,
        "requirement_group_id": group_id
    })
    assert response.status_code == 200
    workex_id = response.json()["milestone_workex_requirement_id"]
    print(f"Workex Requirement Created: {workex_id}")

    # 4. Skill Requirement
    response = client.post("/requirement/skill_requirements/", json={
        "name": "Python Proficiency",
        "dependency_type": "Mandatory",
        "prerequisite_skill_level": "Intermediate",
        "requirement_group_id": group_id
    })
    assert response.status_code == 200
    skill_id = response.json()["milestone_skill_requirement_id"]
    print(f"Skill Requirement Created: {skill_id}")

    # 5. Entrance Requirement
    response = client.post("/requirement/entrance_requirements/", json={
        "name": "SAT",
        "dependency_type": "Mandatory",
        "prerequisite_score_value_min": 1400.0,
        "requirement_group_id": group_id
    })
    assert response.status_code == 200
    entrance_id = response.json()["milestone_entrance_requirement_id"]
    print(f"Entrance Requirement Created: {entrance_id}")

    # 6. Certification Requirement
    response = client.post("/requirement/certification_requirements/", json={
        "name": "AWS Certified Developer",
        "dependency_type": "Benefit",
        "requirement_group_id": group_id
    })
    assert response.status_code == 200
    cert_id = response.json()["milestone_certification_requirement_id"]
    print(f"Certification Requirement Created: {cert_id}")

    # 7. Other Requirement
    response = client.post("/requirement/other_requirements/", json={
        "name": "Portfolio",
        "dependency_type": "Mandatory",
        "prerequisite_description": "Link to GitHub portfolio"
    })
    assert response.status_code == 200
    other_id = response.json()["milestone_other_requirement_id"]
    print(f"Other Requirement Created: {other_id}")

    # Cleanup
    client.delete(f"/requirement/other_requirements/{other_id}")
    client.delete(f"/requirement/certification_requirements/{cert_id}")
    client.delete(f"/requirement/entrance_requirements/{entrance_id}")
    client.delete(f"/requirement/skill_requirements/{skill_id}")
    client.delete(f"/requirement/workex_requirements/{workex_id}")
    client.delete(f"/requirement/academic_requirements/{acad_id}")
    client.delete(f"/requirement/grouping_references/{group_id}")
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_requirement_domain()
        print("All Requirement Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
