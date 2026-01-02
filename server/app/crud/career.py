from sqlalchemy.orm import Session
from ..models import career as models
from ..schemas import career as schemas

# IndustrySector
def get_industry_sector(db: Session, industry_sector_id: int):
    return db.query(models.IndustrySector).filter(models.IndustrySector.industry_sector_id == industry_sector_id).first()

def get_industry_sectors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.IndustrySector).offset(skip).limit(limit).all()

def create_industry_sector(db: Session, industry_sector: schemas.IndustrySectorCreate):
    db_obj = models.IndustrySector(**industry_sector.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_industry_sector(db: Session, industry_sector_id: int, industry_sector: schemas.IndustrySectorUpdate):
    db_obj = get_industry_sector(db, industry_sector_id)
    if db_obj:
        update_data = industry_sector.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_industry_sector(db: Session, industry_sector_id: int):
    db_obj = get_industry_sector(db, industry_sector_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# Industry
def get_industry(db: Session, industry_id: int):
    return db.query(models.Industry).filter(models.Industry.industry_id == industry_id).first()

def get_industries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Industry).offset(skip).limit(limit).all()

def create_industry(db: Session, industry: schemas.IndustryCreate):
    db_obj = models.Industry(**industry.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_industry(db: Session, industry_id: int, industry: schemas.IndustryUpdate):
    db_obj = get_industry(db, industry_id)
    if db_obj:
        update_data = industry.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_industry(db: Session, industry_id: int):
    db_obj = get_industry(db, industry_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# IndustryBranch
def get_industry_branch(db: Session, industry_branch_id: int):
    return db.query(models.IndustryBranch).filter(models.IndustryBranch.industry_branch_id == industry_branch_id).first()

def get_industry_branches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.IndustryBranch).offset(skip).limit(limit).all()

def create_industry_branch(db: Session, industry_branch: schemas.IndustryBranchCreate):
    db_obj = models.IndustryBranch(**industry_branch.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_industry_branch(db: Session, industry_branch_id: int, industry_branch: schemas.IndustryBranchUpdate):
    db_obj = get_industry_branch(db, industry_branch_id)
    if db_obj:
        update_data = industry_branch.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_industry_branch(db: Session, industry_branch_id: int):
    db_obj = get_industry_branch(db, industry_branch_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CareerPosition
def get_career_position(db: Session, career_position_id: int):
    return db.query(models.CareerPosition).filter(models.CareerPosition.career_position_id == career_position_id).first()

def get_career_positions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CareerPosition).offset(skip).limit(limit).all()

def create_career_position(db: Session, career_position: schemas.CareerPositionCreate):
    db_obj = models.CareerPosition(**career_position.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_career_position(db: Session, career_position_id: int, career_position: schemas.CareerPositionUpdate):
    db_obj = get_career_position(db, career_position_id)
    if db_obj:
        update_data = career_position.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_career_position(db: Session, career_position_id: int):
    db_obj = get_career_position(db, career_position_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# SkillCategory
def get_skill_category(db: Session, skill_category_id: int):
    return db.query(models.SkillCategory).filter(models.SkillCategory.skill_category_id == skill_category_id).first()

def get_skill_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SkillCategory).offset(skip).limit(limit).all()

def create_skill_category(db: Session, skill_category: schemas.SkillCategoryCreate):
    db_obj = models.SkillCategory(**skill_category.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_skill_category(db: Session, skill_category_id: int, skill_category: schemas.SkillCategoryUpdate):
    db_obj = get_skill_category(db, skill_category_id)
    if db_obj:
        update_data = skill_category.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_skill_category(db: Session, skill_category_id: int):
    db_obj = get_skill_category(db, skill_category_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# SkillSubcategory
def get_skill_subcategory(db: Session, skill_subcategory_id: int):
    return db.query(models.SkillSubcategory).filter(models.SkillSubcategory.skill_subcategory_id == skill_subcategory_id).first()

def get_skill_subcategories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SkillSubcategory).offset(skip).limit(limit).all()

def create_skill_subcategory(db: Session, skill_subcategory: schemas.SkillSubcategoryCreate):
    db_obj = models.SkillSubcategory(**skill_subcategory.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_skill_subcategory(db: Session, skill_subcategory_id: int, skill_subcategory: schemas.SkillSubcategoryUpdate):
    db_obj = get_skill_subcategory(db, skill_subcategory_id)
    if db_obj:
        update_data = skill_subcategory.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_skill_subcategory(db: Session, skill_subcategory_id: int):
    db_obj = get_skill_subcategory(db, skill_subcategory_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# ScoreReference
def get_score_reference(db: Session, score_reference_id: int):
    return db.query(models.ScoreReference).filter(models.ScoreReference.score_reference_id == score_reference_id).first()

def get_score_references(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ScoreReference).offset(skip).limit(limit).all()

def create_score_reference(db: Session, score_reference: schemas.ScoreReferenceCreate):
    db_obj = models.ScoreReference(**score_reference.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_score_reference(db: Session, score_reference_id: int, score_reference: schemas.ScoreReferenceUpdate):
    db_obj = get_score_reference(db, score_reference_id)
    if db_obj:
        update_data = score_reference.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_score_reference(db: Session, score_reference_id: int):
    db_obj = get_score_reference(db, score_reference_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# SkillSubcategoryCareerPosition (Relationship)
def create_skill_subcategory_career_position(db: Session, relationship: schemas.SkillSubcategoryCareerPositionCreate):
    db_obj = models.SkillSubcategoryCareerPosition(**relationship.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_skill_subcategory_career_position(db: Session, relationship_id: int):
    db_obj = db.query(models.SkillSubcategoryCareerPosition).filter(models.SkillSubcategoryCareerPosition.skill_subcategory_career_position_id == relationship_id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

def get_skills_for_career_position(db: Session, career_position_id: int):
    return db.query(models.SkillSubcategoryCareerPosition).filter(models.SkillSubcategoryCareerPosition.career_position_id == career_position_id).all()
