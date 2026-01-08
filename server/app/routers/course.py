from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import course as schemas
from ..crud import course as crud

router = APIRouter(
    prefix="/course",
    tags=["course"],
    responses={404: {"description": "Not found"}},
)

# TargetStudentType
@router.post("/target_student_types/", response_model=schemas.TargetStudentType)
def create_target_student_type(target_student_type: schemas.TargetStudentTypeCreate, db: Session = Depends(get_db)):
    return crud.create_target_student_type(db=db, target_student_type=target_student_type)

@router.get("/target_student_types/", response_model=List[schemas.TargetStudentType])
def read_target_student_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_target_student_types(db, skip=skip, limit=limit)

@router.get("/target_student_types/{type_id}", response_model=schemas.TargetStudentType)
def read_target_student_type(type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_target_student_type(db, target_student_type_id=type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Target Student Type not found")
    return db_obj

@router.put("/target_student_types/{type_id}", response_model=schemas.TargetStudentType)
def update_target_student_type(type_id: int, target_student_type: schemas.TargetStudentTypeUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_target_student_type(db, target_student_type_id=type_id, target_student_type=target_student_type)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Target Student Type not found")
    return db_obj

@router.delete("/target_student_types/{type_id}", response_model=schemas.TargetStudentType)
def delete_target_student_type(type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_target_student_type(db, target_student_type_id=type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Target Student Type not found")
    return db_obj

# AttendanceType
@router.post("/attendance_types/", response_model=schemas.AttendanceType)
def create_attendance_type(attendance_type: schemas.AttendanceTypeCreate, db: Session = Depends(get_db)):
    return crud.create_attendance_type(db=db, attendance_type=attendance_type)

@router.get("/attendance_types/", response_model=List[schemas.AttendanceType])
def read_attendance_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_attendance_types(db, skip=skip, limit=limit)

@router.get("/attendance_types/{type_id}", response_model=schemas.AttendanceType)
def read_attendance_type(type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_attendance_type(db, attendance_type_id=type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Attendance Type not found")
    return db_obj

@router.put("/attendance_types/{type_id}", response_model=schemas.AttendanceType)
def update_attendance_type(type_id: int, attendance_type: schemas.AttendanceTypeUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_attendance_type(db, attendance_type_id=type_id, attendance_type=attendance_type)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Attendance Type not found")
    return db_obj

@router.delete("/attendance_types/{type_id}", response_model=schemas.AttendanceType)
def delete_attendance_type(type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_attendance_type(db, attendance_type_id=type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Attendance Type not found")
    return db_obj

# CourseSpecific
@router.post("/course_specifics/", response_model=schemas.CourseSpecific)
def create_course_specific(course_specific: schemas.CourseSpecificCreate, db: Session = Depends(get_db)):
    return crud.create_course_specific(db=db, course_specific=course_specific)

@router.get("/course_specifics/", response_model=List[schemas.CourseSpecific])
def read_course_specifics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_course_specifics(db, skip=skip, limit=limit)

@router.get("/course_specifics/{course_id}", response_model=schemas.CourseSpecific)
def read_course_specific(course_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_course_specific(db, course_specific_id=course_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Course Specific not found")
    return db_obj

@router.put("/course_specifics/{course_id}", response_model=schemas.CourseSpecific)
def update_course_specific(course_id: int, course_specific: schemas.CourseSpecificUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_course_specific(db, course_specific_id=course_id, course_specific=course_specific)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Course Specific not found")
    return db_obj

@router.delete("/course_specifics/{course_id}", response_model=schemas.CourseSpecific)
def delete_course_specific(course_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_specific(db, course_specific_id=course_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Course Specific not found")
    return db_obj

# CourseSpecificTargetStudentType
@router.post("/course_target_student_types/", response_model=schemas.CourseSpecificTargetStudentType)
def create_course_target_student_type(mapping: schemas.CourseSpecificTargetStudentTypeCreate, db: Session = Depends(get_db)):
    return crud.create_course_specific_target_student_type(db=db, mapping=mapping)

@router.delete("/course_target_student_types/{mapping_id}", response_model=schemas.CourseSpecificTargetStudentType)
def delete_course_target_student_type(mapping_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_specific_target_student_type(db, mapping_id=mapping_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

# CourseSpecificAttendanceType
@router.post("/course_attendance_types/", response_model=schemas.CourseSpecificAttendanceType)
def create_course_attendance_type(mapping: schemas.CourseSpecificAttendanceTypeCreate, db: Session = Depends(get_db)):
    return crud.create_course_specific_attendance_type(db=db, mapping=mapping)

@router.delete("/course_attendance_types/{mapping_id}", response_model=schemas.CourseSpecificAttendanceType)
def delete_course_attendance_type(mapping_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_specific_attendance_type(db, mapping_id=mapping_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

# CourseSpecificRanking
@router.post("/course_rankings/", response_model=schemas.CourseSpecificRanking)
def create_course_ranking(ranking: schemas.CourseSpecificRankingCreate, db: Session = Depends(get_db)):
    return crud.create_course_specific_ranking(db=db, ranking=ranking)

@router.get("/course_rankings/", response_model=List[schemas.CourseSpecificRanking])
def read_course_rankings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_course_specific_rankings(db, skip=skip, limit=limit)

@router.get("/course_rankings/{ranking_id}", response_model=schemas.CourseSpecificRanking)
def read_course_ranking(ranking_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_course_specific_ranking(db, ranking_id=ranking_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Ranking not found")
    return db_obj

@router.put("/course_rankings/{ranking_id}", response_model=schemas.CourseSpecificRanking)
def update_course_ranking(ranking_id: int, ranking: schemas.CourseSpecificRankingUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_course_specific_ranking(db, ranking_id=ranking_id, ranking=ranking)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Ranking not found")
    return db_obj

@router.delete("/course_rankings/{ranking_id}", response_model=schemas.CourseSpecificRanking)
def delete_course_ranking(ranking_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_specific_ranking(db, ranking_id=ranking_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Ranking not found")
    return db_obj

# CourseSpecificExpense
@router.post("/course_expenses/", response_model=schemas.CourseSpecificExpense)
def create_course_expense(expense: schemas.CourseSpecificExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_course_specific_expense(db=db, expense=expense)

@router.get("/course_expenses/", response_model=List[schemas.CourseSpecificExpense])
def read_course_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_course_specific_expenses(db, skip=skip, limit=limit)

@router.get("/course_expenses/{expense_id}", response_model=schemas.CourseSpecificExpense)
def read_course_expense(expense_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_course_specific_expense(db, expense_id=expense_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_obj

@router.put("/course_expenses/{expense_id}", response_model=schemas.CourseSpecificExpense)
def update_course_expense(expense_id: int, expense: schemas.CourseSpecificExpenseUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_course_specific_expense(db, expense_id=expense_id, expense=expense)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_obj

@router.delete("/course_expenses/{expense_id}", response_model=schemas.CourseSpecificExpense)
def delete_course_expense(expense_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_specific_expense(db, expense_id=expense_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_obj
