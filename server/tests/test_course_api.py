import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to sys.path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_course_domain():
    print("Testing Course Specific Domain APIs...")

    # 1. Target Student Type
    response = client.post("/course/target_student_types/", json={
        "name": "Working Professionals",
        "description": "Designed for employed individuals"
    })
    assert response.status_code == 200
    student_type_id = response.json()["target_student_type_id"]
    print(f"Target Student Type Created: {student_type_id}")

    # 2. Attendance Type
    response = client.post("/course/attendance_types/", json={
        "name": "Hybrid",
        "description": "Mix of online and offline"
    })
    assert response.status_code == 200
    attendance_type_id = response.json()["attendance_type_id"]
    print(f"Attendance Type Created: {attendance_type_id}")

    # 3. Course Specific
    response = client.post("/course/course_specifics/", json={
        "name": "Advanced Python for Data Science",
        "course_type": "Certification",
        "course_tuition_cost_INR": 50000.0,
        "course_duration_months": 6.0
    })
    assert response.status_code == 200
    course_id = response.json()["course_specific_id"]
    print(f"Course Specific Created: {course_id}")

    # 4. Course Specific Target Student Type
    response = client.post("/course/course_target_student_types/", json={
        "course_specific_id": course_id,
        "target_student_type_id": student_type_id
    })
    assert response.status_code == 200
    mapping_student_id = response.json()["course_specific_target_student_type_id"]
    print(f"Course Target Student Type Mapping Created: {mapping_student_id}")

    # 5. Course Specific Attendance Type
    response = client.post("/course/course_attendance_types/", json={
        "course_specific_id": course_id,
        "attendance_type_id": attendance_type_id
    })
    assert response.status_code == 200
    mapping_attendance_id = response.json()["course_specific_attendance_type_id"]
    print(f"Course Attendance Type Mapping Created: {mapping_attendance_id}")

    # 6. Course Specific Ranking
    response = client.post("/course/course_rankings/", json={
        "course_specific_id": course_id,
        "rank": 5,
        "year_of_rank": 2023,
        "description": "Top 5 Data Science Courses"
    })
    assert response.status_code == 200
    ranking_id = response.json()["course_specific_ranking_id"]
    print(f"Course Ranking Created: {ranking_id}")

    # 7. Course Specific Expense
    response = client.post("/course/course_expenses/", json={
        "name": "Lab Fee",
        "course_specific_id": course_id,
        "amount": 5000.0,
        "frequency": "One-time"
    })
    assert response.status_code == 200
    expense_id = response.json()["course_specific_expense_id"]
    print(f"Course Expense Created: {expense_id}")

    # Cleanup
    client.delete(f"/course/course_expenses/{expense_id}")
    client.delete(f"/course/course_rankings/{ranking_id}")
    client.delete(f"/course/course_attendance_types/{mapping_attendance_id}")
    client.delete(f"/course/course_target_student_types/{mapping_student_id}")
    client.delete(f"/course/course_specifics/{course_id}")
    client.delete(f"/course/attendance_types/{attendance_type_id}")
    client.delete(f"/course/target_student_types/{student_type_id}")
    print("Cleanup Complete.")

if __name__ == "__main__":
    try:
        test_course_domain()
        print("All Course Specific Domain tests passed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
