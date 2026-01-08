from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import institution as schemas
from ..crud import institution as crud

router = APIRouter(
    prefix="/institution",
    tags=["institution"],
    responses={404: {"description": "Not found"}},
)

# Institution
@router.post("/institutions/", response_model=schemas.Institution)
def create_institution(institution: schemas.InstitutionCreate, db: Session = Depends(get_db)):
    return crud.create_institution(db=db, institution=institution)

@router.get("/institutions/", response_model=List[schemas.Institution])
def read_institutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_institutions(db, skip=skip, limit=limit)

@router.get("/institutions/{institution_id}", response_model=schemas.Institution)
def read_institution(institution_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_institution(db, institution_id=institution_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Institution not found")
    return db_obj

@router.put("/institutions/{institution_id}", response_model=schemas.Institution)
def update_institution(institution_id: int, institution: schemas.InstitutionUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_institution(db, institution_id=institution_id, institution=institution)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Institution not found")
    return db_obj

@router.delete("/institutions/{institution_id}", response_model=schemas.Institution)
def delete_institution(institution_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_institution(db, institution_id=institution_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Institution not found")
    return db_obj

# InstitutionCategory
@router.post("/categories/", response_model=schemas.InstitutionCategory)
def create_institution_category(institution_category: schemas.InstitutionCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_institution_category(db=db, institution_category=institution_category)

@router.get("/categories/", response_model=List[schemas.InstitutionCategory])
def read_institution_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_institution_categories(db, skip=skip, limit=limit)

@router.get("/categories/{category_id}", response_model=schemas.InstitutionCategory)
def read_institution_category(category_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_institution_category(db, institution_category_id=category_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Institution Category not found")
    return db_obj

@router.put("/categories/{category_id}", response_model=schemas.InstitutionCategory)
def update_institution_category(category_id: int, institution_category: schemas.InstitutionCategoryUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_institution_category(db, institution_category_id=category_id, institution_category=institution_category)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Institution Category not found")
    return db_obj

@router.delete("/categories/{category_id}", response_model=schemas.InstitutionCategory)
def delete_institution_category(category_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_institution_category(db, institution_category_id=category_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Institution Category not found")
    return db_obj

# AssociationAccreditationAffiliation (AAA)
@router.post("/aaa/", response_model=schemas.AAA)
def create_aaa(aaa: schemas.AAACreate, db: Session = Depends(get_db)):
    return crud.create_aaa(db=db, aaa=aaa)

@router.get("/aaa/", response_model=List[schemas.AAA])
def read_aaas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_aaas(db, skip=skip, limit=limit)

@router.get("/aaa/{aaa_id}", response_model=schemas.AAA)
def read_aaa(aaa_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_aaa(db, aaa_id=aaa_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="AAA not found")
    return db_obj

@router.put("/aaa/{aaa_id}", response_model=schemas.AAA)
def update_aaa(aaa_id: int, aaa: schemas.AAAUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_aaa(db, aaa_id=aaa_id, aaa=aaa)
    if not db_obj:
        raise HTTPException(status_code=404, detail="AAA not found")
    return db_obj

@router.delete("/aaa/{aaa_id}", response_model=schemas.AAA)
def delete_aaa(aaa_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_aaa(db, aaa_id=aaa_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="AAA not found")
    return db_obj
