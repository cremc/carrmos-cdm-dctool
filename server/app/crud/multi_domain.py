from sqlalchemy.orm import Session
from ..models import multi_domain as models
from ..schemas import multi_domain as schemas

# DisciplineIndustryBranch (Multi-Domain Relationship)
def create_discipline_industry_branch(db: Session, relationship: schemas.DisciplineIndustryBranchCreate):
    db_obj = models.DisciplineIndustryBranch(**relationship.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_discipline_industry_branch(db: Session, relationship_id: int):
    db_obj = db.query(models.DisciplineIndustryBranch).filter(models.DisciplineIndustryBranch.discipline_industry_branch_id == relationship_id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

def get_industry_branches_for_discipline(db: Session, discipline_id: int):
    return db.query(models.DisciplineIndustryBranch).filter(models.DisciplineIndustryBranch.discipline_id == discipline_id).all()
