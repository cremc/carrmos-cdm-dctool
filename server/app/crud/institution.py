from sqlalchemy.orm import Session
from ..models import institution as models
from ..schemas import institution as schemas

# Institution
def get_institution(db: Session, institution_id: int):
    return db.query(models.Institution).filter(models.Institution.institution_id == institution_id).first()

def get_institutions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Institution).offset(skip).limit(limit).all()

def create_institution(db: Session, institution: schemas.InstitutionCreate):
    db_obj = models.Institution(**institution.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_institution(db: Session, institution_id: int, institution: schemas.InstitutionUpdate):
    db_obj = get_institution(db, institution_id)
    if db_obj:
        update_data = institution.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_institution(db: Session, institution_id: int):
    db_obj = get_institution(db, institution_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# InstitutionCategory
def get_institution_category(db: Session, institution_category_id: int):
    return db.query(models.InstitutionCategory).filter(models.InstitutionCategory.institution_category_id == institution_category_id).first()

def get_institution_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InstitutionCategory).offset(skip).limit(limit).all()

def create_institution_category(db: Session, institution_category: schemas.InstitutionCategoryCreate):
    db_obj = models.InstitutionCategory(**institution_category.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_institution_category(db: Session, institution_category_id: int, institution_category: schemas.InstitutionCategoryUpdate):
    db_obj = get_institution_category(db, institution_category_id)
    if db_obj:
        update_data = institution_category.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_institution_category(db: Session, institution_category_id: int):
    db_obj = get_institution_category(db, institution_category_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# AssociationAccreditationAffiliation (AAA)
def get_aaa(db: Session, aaa_id: int):
    return db.query(models.AssociationAccreditationAffiliation).filter(models.AssociationAccreditationAffiliation.aaa_id == aaa_id).first()

def get_aaas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AssociationAccreditationAffiliation).offset(skip).limit(limit).all()

def create_aaa(db: Session, aaa: schemas.AAACreate):
    db_obj = models.AssociationAccreditationAffiliation(**aaa.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_aaa(db: Session, aaa_id: int, aaa: schemas.AAAUpdate):
    db_obj = get_aaa(db, aaa_id)
    if db_obj:
        update_data = aaa.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_aaa(db: Session, aaa_id: int):
    db_obj = get_aaa(db, aaa_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
