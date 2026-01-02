from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import academics as schemas
from ..crud import academics as crud

router = APIRouter(
    prefix="/academics",
    tags=["academics"],
    responses={404: {"description": "Not found"}},
)

# AcademicLevel
@router.post("/academic_levels/", response_model=schemas.AcademicLevel)
def create_academic_level(academic_level: schemas.AcademicLevelCreate, db: Session = Depends(get_db)):
    return crud.create_academic_level(db=db, academic_level=academic_level)

@router.get("/academic_levels/", response_model=List[schemas.AcademicLevel])
def read_academic_levels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    academic_levels = crud.get_academic_levels(db, skip=skip, limit=limit)
    return academic_levels

@router.get("/academic_levels/{academic_level_id}", response_model=schemas.AcademicLevel)
def read_academic_level(academic_level_id: int, db: Session = Depends(get_db)):
    db_academic_level = crud.get_academic_level(db, academic_level_id=academic_level_id)
    if db_academic_level is None:
        raise HTTPException(status_code=404, detail="Academic Level not found")
    return db_academic_level

@router.put("/academic_levels/{academic_level_id}", response_model=schemas.AcademicLevel)
def update_academic_level(academic_level_id: int, academic_level: schemas.AcademicLevelUpdate, db: Session = Depends(get_db)):
    db_academic_level = crud.update_academic_level(db, academic_level_id=academic_level_id, academic_level=academic_level)
    if db_academic_level is None:
        raise HTTPException(status_code=404, detail="Academic Level not found")
    return db_academic_level

@router.delete("/academic_levels/{academic_level_id}", response_model=schemas.AcademicLevel)
def delete_academic_level(academic_level_id: int, db: Session = Depends(get_db)):
    db_academic_level = crud.delete_academic_level(db, academic_level_id=academic_level_id)
    if db_academic_level is None:
        raise HTTPException(status_code=404, detail="Academic Level not found")
    return db_academic_level

# Stream
@router.post("/streams/", response_model=schemas.Stream)
def create_stream(stream: schemas.StreamCreate, db: Session = Depends(get_db)):
    return crud.create_stream(db=db, stream=stream)

@router.get("/streams/", response_model=List[schemas.Stream])
def read_streams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    streams = crud.get_streams(db, skip=skip, limit=limit)
    return streams

@router.get("/streams/{stream_id}", response_model=schemas.Stream)
def read_stream(stream_id: int, db: Session = Depends(get_db)):
    db_stream = crud.get_stream(db, stream_id=stream_id)
    if db_stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return db_stream

@router.put("/streams/{stream_id}", response_model=schemas.Stream)
def update_stream(stream_id: int, stream: schemas.StreamUpdate, db: Session = Depends(get_db)):
    db_stream = crud.update_stream(db, stream_id=stream_id, stream=stream)
    if db_stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return db_stream

@router.delete("/streams/{stream_id}", response_model=schemas.Stream)
def delete_stream(stream_id: int, db: Session = Depends(get_db)):
    db_stream = crud.delete_stream(db, stream_id=stream_id)
    if db_stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return db_stream

# DisciplineGroup
@router.post("/discipline_groups/", response_model=schemas.DisciplineGroup)
def create_discipline_group(discipline_group: schemas.DisciplineGroupCreate, db: Session = Depends(get_db)):
    return crud.create_discipline_group(db=db, discipline_group=discipline_group)

@router.get("/discipline_groups/", response_model=List[schemas.DisciplineGroup])
def read_discipline_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    discipline_groups = crud.get_discipline_groups(db, skip=skip, limit=limit)
    return discipline_groups

@router.get("/discipline_groups/{discipline_group_id}", response_model=schemas.DisciplineGroup)
def read_discipline_group(discipline_group_id: int, db: Session = Depends(get_db)):
    db_discipline_group = crud.get_discipline_group(db, discipline_group_id=discipline_group_id)
    if db_discipline_group is None:
        raise HTTPException(status_code=404, detail="Discipline Group not found")
    return db_discipline_group

@router.put("/discipline_groups/{discipline_group_id}", response_model=schemas.DisciplineGroup)
def update_discipline_group(discipline_group_id: int, discipline_group: schemas.DisciplineGroupUpdate, db: Session = Depends(get_db)):
    db_discipline_group = crud.update_discipline_group(db, discipline_group_id=discipline_group_id, discipline_group=discipline_group)
    if db_discipline_group is None:
        raise HTTPException(status_code=404, detail="Discipline Group not found")
    return db_discipline_group

@router.delete("/discipline_groups/{discipline_group_id}", response_model=schemas.DisciplineGroup)
def delete_discipline_group(discipline_group_id: int, db: Session = Depends(get_db)):
    db_discipline_group = crud.delete_discipline_group(db, discipline_group_id=discipline_group_id)
    if db_discipline_group is None:
        raise HTTPException(status_code=404, detail="Discipline Group not found")
    return db_discipline_group

# Discipline
@router.post("/disciplines/", response_model=schemas.Discipline)
def create_discipline(discipline: schemas.DisciplineCreate, db: Session = Depends(get_db)):
    return crud.create_discipline(db=db, discipline=discipline)

@router.get("/disciplines/", response_model=List[schemas.Discipline])
def read_disciplines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    disciplines = crud.get_disciplines(db, skip=skip, limit=limit)
    return disciplines

@router.get("/disciplines/{discipline_id}", response_model=schemas.Discipline)
def read_discipline(discipline_id: int, db: Session = Depends(get_db)):
    db_discipline = crud.get_discipline(db, discipline_id=discipline_id)
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline

@router.put("/disciplines/{discipline_id}", response_model=schemas.Discipline)
def update_discipline(discipline_id: int, discipline: schemas.DisciplineUpdate, db: Session = Depends(get_db)):
    db_discipline = crud.update_discipline(db, discipline_id=discipline_id, discipline=discipline)
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline

@router.delete("/disciplines/{discipline_id}", response_model=schemas.Discipline)
def delete_discipline(discipline_id: int, db: Session = Depends(get_db)):
    db_discipline = crud.delete_discipline(db, discipline_id=discipline_id)
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline

# CourseGeneral
@router.post("/course_generals/", response_model=schemas.CourseGeneral)
def create_course_general(course_general: schemas.CourseGeneralCreate, db: Session = Depends(get_db)):
    return crud.create_course_general(db=db, course_general=course_general)

@router.get("/course_generals/", response_model=List[schemas.CourseGeneral])
def read_course_generals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    course_generals = crud.get_course_generals(db, skip=skip, limit=limit)
    return course_generals

@router.get("/course_generals/{course_general_id}", response_model=schemas.CourseGeneral)
def read_course_general(course_general_id: int, db: Session = Depends(get_db)):
    db_course_general = crud.get_course_general(db, course_general_id=course_general_id)
    if db_course_general is None:
        raise HTTPException(status_code=404, detail="Course General not found")
    return db_course_general

@router.put("/course_generals/{course_general_id}", response_model=schemas.CourseGeneral)
def update_course_general(course_general_id: int, course_general: schemas.CourseGeneralUpdate, db: Session = Depends(get_db)):
    db_course_general = crud.update_course_general(db, course_general_id=course_general_id, course_general=course_general)
    if db_course_general is None:
        raise HTTPException(status_code=404, detail="Course General not found")
    return db_course_general

@router.delete("/course_generals/{course_general_id}", response_model=schemas.CourseGeneral)
def delete_course_general(course_general_id: int, db: Session = Depends(get_db)):
    db_course_general = crud.delete_course_general(db, course_general_id=course_general_id)
    if db_course_general is None:
        raise HTTPException(status_code=404, detail="Course General not found")
    return db_course_general

# CoreSubject
@router.post("/core_subjects/", response_model=schemas.CoreSubject)
def create_core_subject(core_subject: schemas.CoreSubjectCreate, db: Session = Depends(get_db)):
    return crud.create_core_subject(db=db, core_subject=core_subject)

@router.get("/core_subjects/", response_model=List[schemas.CoreSubject])
def read_core_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    core_subjects = crud.get_core_subjects(db, skip=skip, limit=limit)
    return core_subjects

@router.get("/core_subjects/{core_subject_id}", response_model=schemas.CoreSubject)
def read_core_subject(core_subject_id: int, db: Session = Depends(get_db)):
    db_core_subject = crud.get_core_subject(db, core_subject_id=core_subject_id)
    if db_core_subject is None:
        raise HTTPException(status_code=404, detail="Core Subject not found")
    return db_core_subject

@router.put("/core_subjects/{core_subject_id}", response_model=schemas.CoreSubject)
def update_core_subject(core_subject_id: int, core_subject: schemas.CoreSubjectUpdate, db: Session = Depends(get_db)):
    db_core_subject = crud.update_core_subject(db, core_subject_id=core_subject_id, core_subject=core_subject)
    if db_core_subject is None:
        raise HTTPException(status_code=404, detail="Core Subject not found")
    return db_core_subject

@router.delete("/core_subjects/{core_subject_id}", response_model=schemas.CoreSubject)
def delete_core_subject(core_subject_id: int, db: Session = Depends(get_db)):
    db_core_subject = crud.delete_core_subject(db, core_subject_id=core_subject_id)
    if db_core_subject is None:
        raise HTTPException(status_code=404, detail="Core Subject not found")
    return db_core_subject

# CourseGeneralCoreSubject (Relationship)
@router.post("/course_generals/core_subjects/", response_model=schemas.CourseGeneralCoreSubject)
def create_course_general_core_subject(relationship: schemas.CourseGeneralCoreSubjectCreate, db: Session = Depends(get_db)):
    return crud.create_course_general_core_subject(db=db, relationship=relationship)

@router.delete("/course_generals/core_subjects/{relationship_id}", response_model=schemas.CourseGeneralCoreSubject)
def delete_course_general_core_subject(relationship_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_general_core_subject(db, relationship_id=relationship_id)
    if not db_obj:
         raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

@router.get("/course_generals/{course_general_id}/core_subjects/", response_model=List[schemas.CourseGeneralCoreSubject])
def read_core_subjects_for_course(course_general_id: int, db: Session = Depends(get_db)):
    return crud.get_core_subjects_for_course(db, course_general_id=course_general_id)

# CourseGeneralDiscipline (Relationship)
@router.post("/course_generals/disciplines/", response_model=schemas.CourseGeneralDiscipline)
def create_course_general_discipline(relationship: schemas.CourseGeneralDisciplineCreate, db: Session = Depends(get_db)):
    return crud.create_course_general_discipline(db=db, relationship=relationship)

@router.delete("/course_generals/disciplines/{relationship_id}", response_model=schemas.CourseGeneralDiscipline)
def delete_course_general_discipline(relationship_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_course_general_discipline(db, relationship_id=relationship_id)
    if not db_obj:
         raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

@router.get("/course_generals/{course_general_id}/disciplines/", response_model=List[schemas.CourseGeneralDiscipline])
def read_disciplines_for_course(course_general_id: int, db: Session = Depends(get_db)):
    return crud.get_disciplines_for_course(db, course_general_id=course_general_id)
