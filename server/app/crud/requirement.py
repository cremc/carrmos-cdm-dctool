from sqlalchemy.orm import Session
from ..models import requirement as models
from ..schemas import requirement as schemas

# GroupingReference
def get_grouping_reference(db: Session, requirement_group_id: int):
    return db.query(models.GroupingReference).filter(models.GroupingReference.requirement_group_id == requirement_group_id).first()

def get_grouping_references(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GroupingReference).offset(skip).limit(limit).all()

def create_grouping_reference(db: Session, grouping_reference: schemas.GroupingReferenceCreate):
    db_obj = models.GroupingReference(**grouping_reference.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_grouping_reference(db: Session, requirement_group_id: int, grouping_reference: schemas.GroupingReferenceUpdate):
    db_obj = get_grouping_reference(db, requirement_group_id)
    if db_obj:
        update_data = grouping_reference.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_grouping_reference(db: Session, requirement_group_id: int):
    db_obj = get_grouping_reference(db, requirement_group_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# MilestoneAcademicRequirement
def get_academic_requirement(db: Session, requirement_id: int):
    return db.query(models.MilestoneAcademicRequirement).filter(models.MilestoneAcademicRequirement.milestone_academic_requirement_id == requirement_id).first()

def get_academic_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilestoneAcademicRequirement).offset(skip).limit(limit).all()

def create_academic_requirement(db: Session, requirement: schemas.MilestoneAcademicRequirementCreate):
    db_obj = models.MilestoneAcademicRequirement(**requirement.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_academic_requirement(db: Session, requirement_id: int, requirement: schemas.MilestoneAcademicRequirementUpdate):
    db_obj = get_academic_requirement(db, requirement_id)
    if db_obj:
        update_data = requirement.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_academic_requirement(db: Session, requirement_id: int):
    db_obj = get_academic_requirement(db, requirement_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# MilestoneWorkexRequirement
def get_workex_requirement(db: Session, requirement_id: int):
    return db.query(models.MilestoneWorkexRequirement).filter(models.MilestoneWorkexRequirement.milestone_workex_requirement_id == requirement_id).first()

def get_workex_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilestoneWorkexRequirement).offset(skip).limit(limit).all()

def create_workex_requirement(db: Session, requirement: schemas.MilestoneWorkexRequirementCreate):
    db_obj = models.MilestoneWorkexRequirement(**requirement.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_workex_requirement(db: Session, requirement_id: int, requirement: schemas.MilestoneWorkexRequirementUpdate):
    db_obj = get_workex_requirement(db, requirement_id)
    if db_obj:
        update_data = requirement.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_workex_requirement(db: Session, requirement_id: int):
    db_obj = get_workex_requirement(db, requirement_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# MilestoneSkillRequirement
def get_skill_requirement(db: Session, requirement_id: int):
    return db.query(models.MilestoneSkillRequirement).filter(models.MilestoneSkillRequirement.milestone_skill_requirement_id == requirement_id).first()

def get_skill_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilestoneSkillRequirement).offset(skip).limit(limit).all()

def create_skill_requirement(db: Session, requirement: schemas.MilestoneSkillRequirementCreate):
    db_obj = models.MilestoneSkillRequirement(**requirement.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_skill_requirement(db: Session, requirement_id: int, requirement: schemas.MilestoneSkillRequirementUpdate):
    db_obj = get_skill_requirement(db, requirement_id)
    if db_obj:
        update_data = requirement.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_skill_requirement(db: Session, requirement_id: int):
    db_obj = get_skill_requirement(db, requirement_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# MilestoneEntranceRequirement
def get_entrance_requirement(db: Session, requirement_id: int):
    return db.query(models.MilestoneEntranceRequirement).filter(models.MilestoneEntranceRequirement.milestone_entrance_requirement_id == requirement_id).first()

def get_entrance_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilestoneEntranceRequirement).offset(skip).limit(limit).all()

def create_entrance_requirement(db: Session, requirement: schemas.MilestoneEntranceRequirementCreate):
    db_obj = models.MilestoneEntranceRequirement(**requirement.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_entrance_requirement(db: Session, requirement_id: int, requirement: schemas.MilestoneEntranceRequirementUpdate):
    db_obj = get_entrance_requirement(db, requirement_id)
    if db_obj:
        update_data = requirement.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_entrance_requirement(db: Session, requirement_id: int):
    db_obj = get_entrance_requirement(db, requirement_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# MilestoneCertificationRequirement
def get_certification_requirement(db: Session, requirement_id: int):
    return db.query(models.MilestoneCertificationRequirement).filter(models.MilestoneCertificationRequirement.milestone_certification_requirement_id == requirement_id).first()

def get_certification_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilestoneCertificationRequirement).offset(skip).limit(limit).all()

def create_certification_requirement(db: Session, requirement: schemas.MilestoneCertificationRequirementCreate):
    db_obj = models.MilestoneCertificationRequirement(**requirement.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_certification_requirement(db: Session, requirement_id: int, requirement: schemas.MilestoneCertificationRequirementUpdate):
    db_obj = get_certification_requirement(db, requirement_id)
    if db_obj:
        update_data = requirement.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_certification_requirement(db: Session, requirement_id: int):
    db_obj = get_certification_requirement(db, requirement_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# MilestoneOtherRequirement
def get_other_requirement(db: Session, requirement_id: int):
    return db.query(models.MilestoneOtherRequirement).filter(models.MilestoneOtherRequirement.milestone_other_requirement_id == requirement_id).first()

def get_other_requirements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilestoneOtherRequirement).offset(skip).limit(limit).all()

def create_other_requirement(db: Session, requirement: schemas.MilestoneOtherRequirementCreate):
    db_obj = models.MilestoneOtherRequirement(**requirement.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_other_requirement(db: Session, requirement_id: int, requirement: schemas.MilestoneOtherRequirementUpdate):
    db_obj = get_other_requirement(db, requirement_id)
    if db_obj:
        update_data = requirement.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_other_requirement(db: Session, requirement_id: int):
    db_obj = get_other_requirement(db, requirement_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
