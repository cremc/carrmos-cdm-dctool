
from app.models.user import User
from app.models.academics import CourseGeneral, EntranceTest, AuditMixin
from app.models.institution import AssociationAccreditationAffiliation
from app.schemas.user import UserCreate, User as UserSchema
from app.schemas.academics import CourseGeneralCreate, EntranceTestCreate
from app.schemas.institution import AAACreate

def verify():
    print("Verifying User Model...")
    user_cols = User.__table__.columns.keys()
    assert "users_id" in user_cols
    assert "first_name" in user_cols
    assert "last_name" in user_cols
    assert "db_role" in user_cols
    assert "full_name" not in user_cols
    assert "is_superuser" not in user_cols
    print("User Model [OK]")

    print("Verifying AuditMixin in Academics...")
    ac_cols = CourseGeneral.__table__.columns.keys()
    assert "created_by" in ac_cols
    assert "created_date" in ac_cols
    assert "updated_by" in ac_cols
    assert "updated_date" in ac_cols
    
    # Check course_duration rename
    assert "course_duration" in ac_cols
    assert "course_duration_months" not in ac_cols
    print("Academics CourseGeneral [OK]")

    print("Verifying EntranceTest...")
    et_cols = EntranceTest.__table__.columns.keys()
    assert "max_score_value" in et_cols
    print("EntranceTest [OK]")

    print("Verifying Institution AAA...")
    aaa_cols = AssociationAccreditationAffiliation.__table__.columns.keys()
    assert "aaa_type" in aaa_cols
    assert "aaa_type_id" not in aaa_cols
    print("Institution AAA [OK]")

    print("Verifying Schemas...")
    # Basic schema instantiation test
    u = UserCreate(email="test@example.com", password="pwd", first_name="A", last_name="B")
    assert u.first_name == "A"
    
    c = CourseGeneralCreate(academic_level_id=1, name="C", course_duration="4 years", course_tuition_cost_inr="50000")
    assert c.course_duration == "4 years"
    
    e = EntranceTestCreate(name="T", max_score_value="100")
    assert e.max_score_value == "100"
    
    a = AAACreate(name="N", aaa_type="Association")
    assert a.aaa_type == "Association"
    print("Schemas [OK]")

if __name__ == "__main__":
    try:
        verify()
        print("\nAll verifications passed successfully!")
    except Exception as e:
        print(f"\nVerification failed: {e}")
        import traceback
        traceback.print_exc()
