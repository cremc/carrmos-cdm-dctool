from sqlalchemy.orm import Session
from ..models import course as models
from ..schemas import course as schemas

# TargetStudentType
def get_target_student_type(db: Session, target_student_type_id: int):
    return db.query(models.TargetStudentType).filter(models.TargetStudentType.target_student_type_id == target_student_type_id).first()

def get_target_student_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TargetStudentType).offset(skip).limit(limit).all()

def create_target_student_type(db: Session, target_student_type: schemas.TargetStudentTypeCreate):
    db_obj = models.TargetStudentType(**target_student_type.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_target_student_type(db: Session, target_student_type_id: int, target_student_type: schemas.TargetStudentTypeUpdate):
    db_obj = get_target_student_type(db, target_student_type_id)
    if db_obj:
        update_data = target_student_type.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_target_student_type(db: Session, target_student_type_id: int):
    db_obj = get_target_student_type(db, target_student_type_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# AttendanceType
def get_attendance_type(db: Session, attendance_type_id: int):
    return db.query(models.AttendanceType).filter(models.AttendanceType.attendance_type_id == attendance_type_id).first()

def get_attendance_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AttendanceType).offset(skip).limit(limit).all()

def create_attendance_type(db: Session, attendance_type: schemas.AttendanceTypeCreate):
    db_obj = models.AttendanceType(**attendance_type.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_attendance_type(db: Session, attendance_type_id: int, attendance_type: schemas.AttendanceTypeUpdate):
    db_obj = get_attendance_type(db, attendance_type_id)
    if db_obj:
        update_data = attendance_type.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_attendance_type(db: Session, attendance_type_id: int):
    db_obj = get_attendance_type(db, attendance_type_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseSpecific
def get_course_specific(db: Session, course_specific_id: int):
    return db.query(models.CourseSpecific).filter(models.CourseSpecific.course_specific_id == course_specific_id).first()

def get_course_specifics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CourseSpecific).offset(skip).limit(limit).all()

def create_course_specific(db: Session, course_specific: schemas.CourseSpecificCreate):
    db_obj = models.CourseSpecific(**course_specific.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_course_specific(db: Session, course_specific_id: int, course_specific: schemas.CourseSpecificUpdate):
    db_obj = get_course_specific(db, course_specific_id)
    if db_obj:
        update_data = course_specific.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_course_specific(db: Session, course_specific_id: int):
    db_obj = get_course_specific(db, course_specific_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseSpecificTargetStudentType
def get_course_specific_target_student_type(db: Session, mapping_id: int):
    return db.query(models.CourseSpecificTargetStudentType).filter(models.CourseSpecificTargetStudentType.course_specific_target_student_type_id == mapping_id).first()

def create_course_specific_target_student_type(db: Session, mapping: schemas.CourseSpecificTargetStudentTypeCreate):
    db_obj = models.CourseSpecificTargetStudentType(**mapping.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_course_specific_target_student_type(db: Session, mapping_id: int):
    db_obj = get_course_specific_target_student_type(db, mapping_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseSpecificAttendanceType
def get_course_specific_attendance_type(db: Session, mapping_id: int):
    return db.query(models.CourseSpecificAttendanceType).filter(models.CourseSpecificAttendanceType.course_specific_attendance_type_id == mapping_id).first()

def create_course_specific_attendance_type(db: Session, mapping: schemas.CourseSpecificAttendanceTypeCreate):
    db_obj = models.CourseSpecificAttendanceType(**mapping.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_course_specific_attendance_type(db: Session, mapping_id: int):
    db_obj = get_course_specific_attendance_type(db, mapping_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseSpecificRanking
def get_course_specific_ranking(db: Session, ranking_id: int):
    return db.query(models.CourseSpecificRanking).filter(models.CourseSpecificRanking.course_specific_ranking_id == ranking_id).first()

def get_course_specific_rankings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CourseSpecificRanking).offset(skip).limit(limit).all()

def create_course_specific_ranking(db: Session, ranking: schemas.CourseSpecificRankingCreate):
    db_obj = models.CourseSpecificRanking(**ranking.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_course_specific_ranking(db: Session, ranking_id: int, ranking: schemas.CourseSpecificRankingUpdate):
    db_obj = get_course_specific_ranking(db, ranking_id)
    if db_obj:
        update_data = ranking.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_course_specific_ranking(db: Session, ranking_id: int):
    db_obj = get_course_specific_ranking(db, ranking_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseSpecificExpense
def get_course_specific_expense(db: Session, expense_id: int):
    return db.query(models.CourseSpecificExpense).filter(models.CourseSpecificExpense.course_specific_expense_id == expense_id).first()

def get_course_specific_expenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CourseSpecificExpense).offset(skip).limit(limit).all()

def create_course_specific_expense(db: Session, expense: schemas.CourseSpecificExpenseCreate):
    db_obj = models.CourseSpecificExpense(**expense.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_course_specific_expense(db: Session, expense_id: int, expense: schemas.CourseSpecificExpenseUpdate):
    db_obj = get_course_specific_expense(db, expense_id)
    if db_obj:
        update_data = expense.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_course_specific_expense(db: Session, expense_id: int):
    db_obj = get_course_specific_expense(db, expense_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
