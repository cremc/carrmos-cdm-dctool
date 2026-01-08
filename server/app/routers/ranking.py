from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import ranking as schemas
from ..crud import ranking as crud

router = APIRouter(
    prefix="/ranking",
    tags=["ranking"],
    responses={404: {"description": "Not found"}},
)

# RankingSource
@router.post("/sources/", response_model=schemas.RankingSource)
def create_ranking_source(ranking_source: schemas.RankingSourceCreate, db: Session = Depends(get_db)):
    return crud.create_ranking_source(db=db, ranking_source=ranking_source)

@router.get("/sources/", response_model=List[schemas.RankingSource])
def read_ranking_sources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_ranking_sources(db, skip=skip, limit=limit)

@router.get("/sources/{ranking_source_id}", response_model=schemas.RankingSource)
def read_ranking_source(ranking_source_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_ranking_source(db, ranking_source_id=ranking_source_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Ranking Source not found")
    return db_obj

@router.put("/sources/{ranking_source_id}", response_model=schemas.RankingSource)
def update_ranking_source(ranking_source_id: int, ranking_source: schemas.RankingSourceUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_ranking_source(db, ranking_source_id=ranking_source_id, ranking_source=ranking_source)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Ranking Source not found")
    return db_obj

@router.delete("/sources/{ranking_source_id}", response_model=schemas.RankingSource)
def delete_ranking_source(ranking_source_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_ranking_source(db, ranking_source_id=ranking_source_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Ranking Source not found")
    return db_obj
