import sys
import os
from fastapi.testclient import TestClient
import pytest

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_career_domain():
    print("Testing Career Domain APIs...")

    # 1. Industry Sector
    response = client.post("/career/industry_sectors/", json={"name": "Technology", "description": "IT and Software"})
    assert response.status_code == 200
    sector_id = response.json()["industry_sector_id"]
    print(f"Industry Sector Created: {sector_id}")

    # 2. Industry
    response = client.post("/career/industries/", json={
        "industry_name": "Software Development",
        "description": "Building software",
        "industry_sector_id": sector_id
    })
    assert response.status_code == 200
    industry_id = response.json()["industry_id"]
    print(f"Industry Created: {industry_id}")

    # 3. Industry Branch
    response = client.post("/career/industry_branches/", json={
        "name": "Backend Development",
        "description": "Server side logic",
        "industry_id": industry_id
    })
    assert response.status_code == 200
    branch_id = response.json()["industry_branch_id"]
    print(f"Industry Branch Created: {branch_id}")

    # 4. Career Position
    response = client.post("/career/career_positions/", json={
        "name": "Software Engineer",
        "industry_branch_id": branch_id,
        "industry_id": industry_id,
        "salary_range": "High"
    })
    assert response.status_code == 200
    position_id = response.json()["career_position_id"]
    print(f"Career Position Created: {position_id}")

    # 5. Skill Category
    response = client.post("/career/skill_categories/", json={"name": "Technical", "description": "Hard skills"})
    assert response.status_code == 200
    skill_cat_id = response.json()["skill_category_id"]
    print(f"Skill Category Created: {skill_cat_id}")

    # 6. Skill Subcategory
    response = client.post("/career/skill_subcategories/", json={
        "name": "Python",
        "skill_category_id": skill_cat_id,
        "skill_class": "Programming"
    })
    assert response.status_code == 200
    skill_sub_id = response.json()["skill_subcategory_id"]
    print(f"Skill Subcategory Created: {skill_sub_id}")

    # 7. Score Reference
    response = client.post("/career/score_references/", json={
        "name": "Proficiency 1-5",
        "score_min_value": 1,
        "score_max_value": 5,
        "score_min_max_type": "absolute"
    })
    assert response.status_code == 200
    score_ref_id = response.json()["score_reference_id"]
    print(f"Score Reference Created: {score_ref_id}")

    # 8. Relationship: Skill -> Career Position
    response = client.post("/career/career_positions/skills/", json={
        "skill_subcategory_id": skill_sub_id,
        "career_position_id": position_id,
        "score_reference_id": score_ref_id,
        "skill_level": "High"
    })
    assert response.status_code == 200
    skill_rel_id = response.json()["skill_subcategory_career_position_id"]
    print(f"Skill-Position Relationship Created: {skill_rel_id}")

    # 9. Verify Relationship
    response = client.get(f"/career/career_positions/{position_id}/skills/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print("Skill-Position Relationship Verified.")

    # 10. Multi-domain: Discipline -> Industry Branch
    
    # Create Stream
    s_resp = client.post("/academics/streams/", json={"name": "Integration Test Stream"})
    s_id = s_resp.json()["stream_id"]
    
    # Create Group
    dg_resp = client.post("/academics/discipline_groups/", json={"name": "Integration Group", "stream_id": s_id})
    dg_id = dg_resp.json()["discipline_group_id"]

    # Create Discipline
    d_resp = client.post("/academics/disciplines/", json={"name": "Computer Science", "discipline_group_id": dg_id})
    d_id = d_resp.json()["discipline_id"]

    # Link Discipline -> Industry Branch
    response = client.post("/career/multi/discipline_industry_branches/", json={
        "discipline_id": d_id,
        "industry_branch_id": branch_id,
        "name": "CS -> Backend"
    })
    assert response.status_code == 200
    multi_rel_id = response.json()["discipline_industry_branch_id"]
    print(f"Discipline-Industry Branch Relationship Created: {multi_rel_id}")

    # Verify Multi-domain Link
    response = client.get(f"/career/multi/disciplines/{d_id}/industry_branches/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print("Multi-domain Relationship Verified.")

    # Cleanup (Optional, but good practice for test scripts running on local DB)
    # Deleting in reverse order of creation to avoid FK constraint issues
    client.delete(f"/career/multi/discipline_industry_branches/{multi_rel_id}")
    client.delete(f"/academics/disciplines/{d_id}")
    client.delete(f"/academics/discipline_groups/{dg_id}")
    client.delete(f"/academics/streams/{s_id}")
    client.delete(f"/career/career_positions/skills/{skill_rel_id}")
    client.delete(f"/career/score_references/{score_ref_id}")
    client.delete(f"/career/skill_subcategories/{skill_sub_id}")
    client.delete(f"/career/skill_categories/{skill_cat_id}")
    client.delete(f"/career/career_positions/{position_id}")
    client.delete(f"/career/industry_branches/{branch_id}")
    client.delete(f"/career/industries/{industry_id}")
    client.delete(f"/career/industry_sectors/{sector_id}")
    
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_career_domain()
        print("All Career Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
