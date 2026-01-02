from sqlalchemy.orm import Session
from ..models import academics as models
from ..schemas import academics as schemas

# Helper for generic CRUD? For now, I'll write explicit functions to be safe and clear.

# AcademicLevel
def get_academic_level(db: Session, academic_level_id: int):
    return db.query(models.AcademicLevel).filter(models.AcademicLevel.academic_level_id == academic_level_id).first()

def get_academic_levels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AcademicLevel).offset(skip).limit(limit).all()

def create_academic_level(db: Session, academic_level: schemas.AcademicLevelCreate):
    db_obj = models.AcademicLevel(**academic_level.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_academic_level(db: Session, academic_level_id: int, academic_level: schemas.AcademicLevelUpdate):
    db_obj = get_academic_level(db, academic_level_id)
    if db_obj:
        update_data = academic_level.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_academic_level(db: Session, academic_level_id: int):
    db_obj = get_academic_level(db, academic_level_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# Stream
def get_stream(db: Session, stream_id: int):
    return db.query(models.Stream).filter(models.Stream.stream_id == stream_id).first()

def get_streams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stream).offset(skip).limit(limit).all()

def create_stream(db: Session, stream: schemas.StreamCreate):
    db_obj = models.Stream(**stream.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_stream(db: Session, stream_id: int, stream: schemas.StreamUpdate):
    db_obj = get_stream(db, stream_id)
    if db_obj:
        update_data = stream.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_stream(db: Session, stream_id: int):
    db_obj = get_stream(db, stream_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# DisciplineGroup
def get_discipline_group(db: Session, discipline_group_id: int):
    return db.query(models.DisciplineGroup).filter(models.DisciplineGroup.discipline_group_id == discipline_group_id).first()

def get_discipline_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DisciplineGroup).offset(skip).limit(limit).all()

def create_discipline_group(db: Session, discipline_group: schemas.DisciplineGroupCreate):
    db_obj = models.DisciplineGroup(**discipline_group.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_discipline_group(db: Session, discipline_group_id: int, discipline_group: schemas.DisciplineGroupUpdate):
    db_obj = get_discipline_group(db, discipline_group_id)
    if db_obj:
        update_data = discipline_group.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_discipline_group(db: Session, discipline_group_id: int):
    db_obj = get_discipline_group(db, discipline_group_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# Discipline
def get_discipline(db: Session, discipline_id: int):
    return db.query(models.Discipline).filter(models.Discipline.discipline_id == discipline_id).first()

def get_disciplines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Discipline).offset(skip).limit(limit).all()

def create_discipline(db: Session, discipline: schemas.DisciplineCreate):
    db_obj = models.Discipline(**discipline.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_discipline(db: Session, discipline_id: int, discipline: schemas.DisciplineUpdate):
    db_obj = get_discipline(db, discipline_id)
    if db_obj:
        update_data = discipline.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_discipline(db: Session, discipline_id: int):
    db_obj = get_discipline(db, discipline_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseGeneral
def get_course_general(db: Session, course_general_id: int):
    return db.query(models.CourseGeneral).filter(models.CourseGeneral.course_general_id == course_general_id).first()

def get_course_generals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CourseGeneral).offset(skip).limit(limit).all()

def create_course_general(db: Session, course_general: schemas.CourseGeneralCreate):
    db_obj = models.CourseGeneral(**course_general.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_course_general(db: Session, course_general_id: int, course_general: schemas.CourseGeneralUpdate):
    db_obj = get_course_general(db, course_general_id)
    if db_obj:
        update_data = course_general.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_course_general(db: Session, course_general_id: int):
    db_obj = get_course_general(db, course_general_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CoreSubject
def get_core_subject(db: Session, core_subject_id: int):
    return db.query(models.CoreSubject).filter(models.CoreSubject.core_subject_id == core_subject_id).first()

def get_core_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CoreSubject).offset(skip).limit(limit).all()

def create_core_subject(db: Session, core_subject: schemas.CoreSubjectCreate):
    db_obj = models.CoreSubject(**core_subject.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_core_subject(db: Session, core_subject_id: int, core_subject: schemas.CoreSubjectUpdate):
    db_obj = get_core_subject(db, core_subject_id)
    if db_obj:
        update_data = core_subject.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_core_subject(db: Session, core_subject_id: int):
    db_obj = get_core_subject(db, core_subject_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CourseGeneralCoreSubject (Relationship)
def create_course_general_core_subject(db: Session, relationship: schemas.CourseGeneralCoreSubjectCreate):
    db_obj = models.CourseGeneralCoreSubject(**relationship.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_course_general_core_subject(db: Session, relationship_id: int):
    db_obj = db.query(models.CourseGeneralCoreSubject).filter(models.CourseGeneralCoreSubject.course_general_core_subject_id == relationship_id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

def get_core_subjects_for_course(db: Session, course_general_id: int):
    return db.query(models.CourseGeneralCoreSubject).filter(models.CourseGeneralCoreSubject.course_general_id == course_general_id).all()

# CourseGeneralDiscipline (Relationship)
def create_course_general_discipline(db: Session, relationship: schemas.CourseGeneralDisciplineCreate):
    db_obj = models.CourseGeneralDiscipline(**relationship.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_course_general_discipline(db: Session, relationship_id: int):
    db_obj = db.query(models.CourseGeneralDiscipline).filter(models.CourseGeneralDiscipline.course_general_discipline_id == relationship_id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

def get_disciplines_for_course(db: Session, course_general_id: int):
    return db.query(models.CourseGeneralDiscipline).filter(models.CourseGeneralDiscipline.course_general_id == course_general_id).all()
