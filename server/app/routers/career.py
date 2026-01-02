from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import career as schemas
from ..schemas import multi_domain as md_schemas
from ..crud import career as crud
from ..crud import multi_domain as md_crud

router = APIRouter(
    prefix="/career",
    tags=["career"],
    responses={404: {"description": "Not found"}},
)

# IndustrySector
@router.post("/industry_sectors/", response_model=schemas.IndustrySector)
def create_industry_sector(industry_sector: schemas.IndustrySectorCreate, db: Session = Depends(get_db)):
    return crud.create_industry_sector(db=db, industry_sector=industry_sector)

@router.get("/industry_sectors/", response_model=List[schemas.IndustrySector])
def read_industry_sectors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_industry_sectors(db, skip=skip, limit=limit)

@router.get("/industry_sectors/{industry_sector_id}", response_model=schemas.IndustrySector)
def read_industry_sector(industry_sector_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_industry_sector(db, industry_sector_id=industry_sector_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry Sector not found")
    return db_obj

@router.put("/industry_sectors/{industry_sector_id}", response_model=schemas.IndustrySector)
def update_industry_sector(industry_sector_id: int, industry_sector: schemas.IndustrySectorUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_industry_sector(db, industry_sector_id=industry_sector_id, industry_sector=industry_sector)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry Sector not found")
    return db_obj

@router.delete("/industry_sectors/{industry_sector_id}", response_model=schemas.IndustrySector)
def delete_industry_sector(industry_sector_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_industry_sector(db, industry_sector_id=industry_sector_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry Sector not found")
    return db_obj

# Industry
@router.post("/industries/", response_model=schemas.Industry)
def create_industry(industry: schemas.IndustryCreate, db: Session = Depends(get_db)):
    return crud.create_industry(db=db, industry=industry)

@router.get("/industries/", response_model=List[schemas.Industry])
def read_industries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_industries(db, skip=skip, limit=limit)

@router.get("/industries/{industry_id}", response_model=schemas.Industry)
def read_industry(industry_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_industry(db, industry_id=industry_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry not found")
    return db_obj

@router.put("/industries/{industry_id}", response_model=schemas.Industry)
def update_industry(industry_id: int, industry: schemas.IndustryUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_industry(db, industry_id=industry_id, industry=industry)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry not found")
    return db_obj

@router.delete("/industries/{industry_id}", response_model=schemas.Industry)
def delete_industry(industry_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_industry(db, industry_id=industry_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry not found")
    return db_obj

# IndustryBranch
@router.post("/industry_branches/", response_model=schemas.IndustryBranch)
def create_industry_branch(industry_branch: schemas.IndustryBranchCreate, db: Session = Depends(get_db)):
    return crud.create_industry_branch(db=db, industry_branch=industry_branch)

@router.get("/industry_branches/", response_model=List[schemas.IndustryBranch])
def read_industry_branches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_industry_branches(db, skip=skip, limit=limit)

@router.get("/industry_branches/{industry_branch_id}", response_model=schemas.IndustryBranch)
def read_industry_branch(industry_branch_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_industry_branch(db, industry_branch_id=industry_branch_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry Branch not found")
    return db_obj

@router.put("/industry_branches/{industry_branch_id}", response_model=schemas.IndustryBranch)
def update_industry_branch(industry_branch_id: int, industry_branch: schemas.IndustryBranchUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_industry_branch(db, industry_branch_id=industry_branch_id, industry_branch=industry_branch)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry Branch not found")
    return db_obj

@router.delete("/industry_branches/{industry_branch_id}", response_model=schemas.IndustryBranch)
def delete_industry_branch(industry_branch_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_industry_branch(db, industry_branch_id=industry_branch_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Industry Branch not found")
    return db_obj

# CareerPosition
@router.post("/career_positions/", response_model=schemas.CareerPosition)
def create_career_position(career_position: schemas.CareerPositionCreate, db: Session = Depends(get_db)):
    return crud.create_career_position(db=db, career_position=career_position)

@router.get("/career_positions/", response_model=List[schemas.CareerPosition])
def read_career_positions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_career_positions(db, skip=skip, limit=limit)

@router.get("/career_positions/{career_position_id}", response_model=schemas.CareerPosition)
def read_career_position(career_position_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_career_position(db, career_position_id=career_position_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Career Position not found")
    return db_obj

@router.put("/career_positions/{career_position_id}", response_model=schemas.CareerPosition)
def update_career_position(career_position_id: int, career_position: schemas.CareerPositionUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_career_position(db, career_position_id=career_position_id, career_position=career_position)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Career Position not found")
    return db_obj

@router.delete("/career_positions/{career_position_id}", response_model=schemas.CareerPosition)
def delete_career_position(career_position_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_career_position(db, career_position_id=career_position_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Career Position not found")
    return db_obj

# SkillCategory
@router.post("/skill_categories/", response_model=schemas.SkillCategory)
def create_skill_category(skill_category: schemas.SkillCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_skill_category(db=db, skill_category=skill_category)

@router.get("/skill_categories/", response_model=List[schemas.SkillCategory])
def read_skill_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_skill_categories(db, skip=skip, limit=limit)

@router.get("/skill_categories/{skill_category_id}", response_model=schemas.SkillCategory)
def read_skill_category(skill_category_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_skill_category(db, skill_category_id=skill_category_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Category not found")
    return db_obj

@router.put("/skill_categories/{skill_category_id}", response_model=schemas.SkillCategory)
def update_skill_category(skill_category_id: int, skill_category: schemas.SkillCategoryUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_skill_category(db, skill_category_id=skill_category_id, skill_category=skill_category)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Category not found")
    return db_obj

@router.delete("/skill_categories/{skill_category_id}", response_model=schemas.SkillCategory)
def delete_skill_category(skill_category_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_skill_category(db, skill_category_id=skill_category_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Category not found")
    return db_obj

# SkillSubcategory
@router.post("/skill_subcategories/", response_model=schemas.SkillSubcategory)
def create_skill_subcategory(skill_subcategory: schemas.SkillSubcategoryCreate, db: Session = Depends(get_db)):
    return crud.create_skill_subcategory(db=db, skill_subcategory=skill_subcategory)

@router.get("/skill_subcategories/", response_model=List[schemas.SkillSubcategory])
def read_skill_subcategories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_skill_subcategories(db, skip=skip, limit=limit)

@router.get("/skill_subcategories/{skill_subcategory_id}", response_model=schemas.SkillSubcategory)
def read_skill_subcategory(skill_subcategory_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_skill_subcategory(db, skill_subcategory_id=skill_subcategory_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Subcategory not found")
    return db_obj

@router.put("/skill_subcategories/{skill_subcategory_id}", response_model=schemas.SkillSubcategory)
def update_skill_subcategory(skill_subcategory_id: int, skill_subcategory: schemas.SkillSubcategoryUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_skill_subcategory(db, skill_subcategory_id=skill_subcategory_id, skill_subcategory=skill_subcategory)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Subcategory not found")
    return db_obj

@router.delete("/skill_subcategories/{skill_subcategory_id}", response_model=schemas.SkillSubcategory)
def delete_skill_subcategory(skill_subcategory_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_skill_subcategory(db, skill_subcategory_id=skill_subcategory_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Skill Subcategory not found")
    return db_obj

# ScoreReference
@router.post("/score_references/", response_model=schemas.ScoreReference)
def create_score_reference(score_reference: schemas.ScoreReferenceCreate, db: Session = Depends(get_db)):
    return crud.create_score_reference(db=db, score_reference=score_reference)

@router.get("/score_references/", response_model=List[schemas.ScoreReference])
def read_score_references(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_score_references(db, skip=skip, limit=limit)

@router.get("/score_references/{score_reference_id}", response_model=schemas.ScoreReference)
def read_score_reference(score_reference_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_score_reference(db, score_reference_id=score_reference_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Score Reference not found")
    return db_obj

@router.put("/score_references/{score_reference_id}", response_model=schemas.ScoreReference)
def update_score_reference(score_reference_id: int, score_reference: schemas.ScoreReferenceUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_score_reference(db, score_reference_id=score_reference_id, score_reference=score_reference)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Score Reference not found")
    return db_obj

@router.delete("/score_references/{score_reference_id}", response_model=schemas.ScoreReference)
def delete_score_reference(score_reference_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_score_reference(db, score_reference_id=score_reference_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Score Reference not found")
    return db_obj

# SkillSubcategoryCareerPosition (Relationship)
@router.post("/career_positions/skills/", response_model=schemas.SkillSubcategoryCareerPosition)
def create_skill_subcategory_career_position(relationship: schemas.SkillSubcategoryCareerPositionCreate, db: Session = Depends(get_db)):
    return crud.create_skill_subcategory_career_position(db=db, relationship=relationship)

@router.delete("/career_positions/skills/{relationship_id}", response_model=schemas.SkillSubcategoryCareerPosition)
def delete_skill_subcategory_career_position(relationship_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_skill_subcategory_career_position(db, relationship_id=relationship_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

@router.get("/career_positions/{career_position_id}/skills/", response_model=List[schemas.SkillSubcategoryCareerPosition])
def read_skills_for_career_position(career_position_id: int, db: Session = Depends(get_db)):
    return crud.get_skills_for_career_position(db, career_position_id=career_position_id)

# DisciplineIndustryBranch (Multi-Domain Relationship)
@router.post("/multi/discipline_industry_branches/", response_model=md_schemas.DisciplineIndustryBranch)
def create_discipline_industry_branch(relationship: md_schemas.DisciplineIndustryBranchCreate, db: Session = Depends(get_db)):
    return md_crud.create_discipline_industry_branch(db=db, relationship=relationship)

@router.delete("/multi/discipline_industry_branches/{relationship_id}", response_model=md_schemas.DisciplineIndustryBranch)
def delete_discipline_industry_branch(relationship_id: int, db: Session = Depends(get_db)):
    db_obj = md_crud.delete_discipline_industry_branch(db, relationship_id=relationship_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

@router.get("/multi/disciplines/{discipline_id}/industry_branches/", response_model=List[md_schemas.DisciplineIndustryBranch])
def read_industry_branches_for_discipline(discipline_id: int, db: Session = Depends(get_db)):
    return md_crud.get_industry_branches_for_discipline(db, discipline_id=discipline_id)
