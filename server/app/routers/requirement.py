from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import requirement as schemas
from ..crud import requirement as crud

router = APIRouter(
    prefix="/requirement",
    tags=["requirement"],
    responses={404: {"description": "Not found"}},
)

# GroupingReference
@router.post("/grouping_references/", response_model=schemas.GroupingReference)
def create_grouping_reference(grouping_reference: schemas.GroupingReferenceCreate, db: Session = Depends(get_db)):
    return crud.create_grouping_reference(db=db, grouping_reference=grouping_reference)

@router.get("/grouping_references/", response_model=List[schemas.GroupingReference])
def read_grouping_references(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_grouping_references(db, skip=skip, limit=limit)

@router.get("/grouping_references/{group_id}", response_model=schemas.GroupingReference)
def read_grouping_reference(group_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_grouping_reference(db, requirement_group_id=group_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Grouping Reference not found")
    return db_obj

@router.put("/grouping_references/{group_id}", response_model=schemas.GroupingReference)
def update_grouping_reference(group_id: int, grouping_reference: schemas.GroupingReferenceUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_grouping_reference(db, requirement_group_id=group_id, grouping_reference=grouping_reference)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Grouping Reference not found")
    return db_obj

@router.delete("/grouping_references/{group_id}", response_model=schemas.GroupingReference)
def delete_grouping_reference(group_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_grouping_reference(db, requirement_group_id=group_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Grouping Reference not found")
    return db_obj

# MilestoneAcademicRequirement
@router.post("/academic_requirements/", response_model=schemas.MilestoneAcademicRequirement)
def create_academic_requirement(requirement: schemas.MilestoneAcademicRequirementCreate, db: Session = Depends(get_db)):
    return crud.create_academic_requirement(db=db, requirement=requirement)

@router.get("/academic_requirements/", response_model=List[schemas.MilestoneAcademicRequirement])
def read_academic_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_academic_requirements(db, skip=skip, limit=limit)

@router.get("/academic_requirements/{requirement_id}", response_model=schemas.MilestoneAcademicRequirement)
def read_academic_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_academic_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Academic Requirement not found")
    return db_obj

@router.put("/academic_requirements/{requirement_id}", response_model=schemas.MilestoneAcademicRequirement)
def update_academic_requirement(requirement_id: int, requirement: schemas.MilestoneAcademicRequirementUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_academic_requirement(db, requirement_id=requirement_id, requirement=requirement)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Academic Requirement not found")
    return db_obj

@router.delete("/academic_requirements/{requirement_id}", response_model=schemas.MilestoneAcademicRequirement)
def delete_academic_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_academic_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Academic Requirement not found")
    return db_obj

# MilestoneWorkexRequirement
@router.post("/workex_requirements/", response_model=schemas.MilestoneWorkexRequirement)
def create_workex_requirement(requirement: schemas.MilestoneWorkexRequirementCreate, db: Session = Depends(get_db)):
    return crud.create_workex_requirement(db=db, requirement=requirement)

@router.get("/workex_requirements/", response_model=List[schemas.MilestoneWorkexRequirement])
def read_workex_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_workex_requirements(db, skip=skip, limit=limit)

@router.get("/workex_requirements/{requirement_id}", response_model=schemas.MilestoneWorkexRequirement)
def read_workex_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_workex_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Workex Requirement not found")
    return db_obj

@router.put("/workex_requirements/{requirement_id}", response_model=schemas.MilestoneWorkexRequirement)
def update_workex_requirement(requirement_id: int, requirement: schemas.MilestoneWorkexRequirementUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_workex_requirement(db, requirement_id=requirement_id, requirement=requirement)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Workex Requirement not found")
    return db_obj

@router.delete("/workex_requirements/{requirement_id}", response_model=schemas.MilestoneWorkexRequirement)
def delete_workex_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_workex_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Workex Requirement not found")
    return db_obj

# MilestoneSkillRequirement
@router.post("/skill_requirements/", response_model=schemas.MilestoneSkillRequirement)
def create_skill_requirement(requirement: schemas.MilestoneSkillRequirementCreate, db: Session = Depends(get_db)):
    return crud.create_skill_requirement(db=db, requirement=requirement)

@router.get("/skill_requirements/", response_model=List[schemas.MilestoneSkillRequirement])
def read_skill_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_skill_requirements(db, skip=skip, limit=limit)

@router.get("/skill_requirements/{requirement_id}", response_model=schemas.MilestoneSkillRequirement)
def read_skill_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_skill_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Requirement not found")
    return db_obj

@router.put("/skill_requirements/{requirement_id}", response_model=schemas.MilestoneSkillRequirement)
def update_skill_requirement(requirement_id: int, requirement: schemas.MilestoneSkillRequirementUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_skill_requirement(db, requirement_id=requirement_id, requirement=requirement)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Requirement not found")
    return db_obj

@router.delete("/skill_requirements/{requirement_id}", response_model=schemas.MilestoneSkillRequirement)
def delete_skill_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_skill_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Requirement not found")
    return db_obj

# MilestoneEntranceRequirement
@router.post("/entrance_requirements/", response_model=schemas.MilestoneEntranceRequirement)
def create_entrance_requirement(requirement: schemas.MilestoneEntranceRequirementCreate, db: Session = Depends(get_db)):
    return crud.create_entrance_requirement(db=db, requirement=requirement)

@router.get("/entrance_requirements/", response_model=List[schemas.MilestoneEntranceRequirement])
def read_entrance_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_entrance_requirements(db, skip=skip, limit=limit)

@router.get("/entrance_requirements/{requirement_id}", response_model=schemas.MilestoneEntranceRequirement)
def read_entrance_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_entrance_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Entrance Requirement not found")
    return db_obj

@router.put("/entrance_requirements/{requirement_id}", response_model=schemas.MilestoneEntranceRequirement)
def update_entrance_requirement(requirement_id: int, requirement: schemas.MilestoneEntranceRequirementUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_entrance_requirement(db, requirement_id=requirement_id, requirement=requirement)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Entrance Requirement not found")
    return db_obj

@router.delete("/entrance_requirements/{requirement_id}", response_model=schemas.MilestoneEntranceRequirement)
def delete_entrance_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_entrance_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Entrance Requirement not found")
    return db_obj

# MilestoneCertificationRequirement
@router.post("/certification_requirements/", response_model=schemas.MilestoneCertificationRequirement)
def create_certification_requirement(requirement: schemas.MilestoneCertificationRequirementCreate, db: Session = Depends(get_db)):
    return crud.create_certification_requirement(db=db, requirement=requirement)

@router.get("/certification_requirements/", response_model=List[schemas.MilestoneCertificationRequirement])
def read_certification_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_certification_requirements(db, skip=skip, limit=limit)

@router.get("/certification_requirements/{requirement_id}", response_model=schemas.MilestoneCertificationRequirement)
def read_certification_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_certification_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Certification Requirement not found")
    return db_obj

@router.put("/certification_requirements/{requirement_id}", response_model=schemas.MilestoneCertificationRequirement)
def update_certification_requirement(requirement_id: int, requirement: schemas.MilestoneCertificationRequirementUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_certification_requirement(db, requirement_id=requirement_id, requirement=requirement)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Certification Requirement not found")
    return db_obj

@router.delete("/certification_requirements/{requirement_id}", response_model=schemas.MilestoneCertificationRequirement)
def delete_certification_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_certification_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Certification Requirement not found")
    return db_obj

# MilestoneOtherRequirement
@router.post("/other_requirements/", response_model=schemas.MilestoneOtherRequirement)
def create_other_requirement(requirement: schemas.MilestoneOtherRequirementCreate, db: Session = Depends(get_db)):
    return crud.create_other_requirement(db=db, requirement=requirement)

@router.get("/other_requirements/", response_model=List[schemas.MilestoneOtherRequirement])
def read_other_requirements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_other_requirements(db, skip=skip, limit=limit)

@router.get("/other_requirements/{requirement_id}", response_model=schemas.MilestoneOtherRequirement)
def read_other_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_other_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Other Requirement not found")
    return db_obj

@router.put("/other_requirements/{requirement_id}", response_model=schemas.MilestoneOtherRequirement)
def update_other_requirement(requirement_id: int, requirement: schemas.MilestoneOtherRequirementUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_other_requirement(db, requirement_id=requirement_id, requirement=requirement)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Other Requirement not found")
    return db_obj

@router.delete("/other_requirements/{requirement_id}", response_model=schemas.MilestoneOtherRequirement)
def delete_other_requirement(requirement_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_other_requirement(db, requirement_id=requirement_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Other Requirement not found")
    return db_obj
