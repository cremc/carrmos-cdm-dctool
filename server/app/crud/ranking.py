from sqlalchemy.orm import Session
from ..models import ranking as models
from ..schemas import ranking as schemas

# RankingSource
def get_ranking_source(db: Session, ranking_source_id: int):
    return db.query(models.RankingSource).filter(models.RankingSource.ranking_source_id == ranking_source_id).first()

def get_ranking_sources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RankingSource).offset(skip).limit(limit).all()

def create_ranking_source(db: Session, ranking_source: schemas.RankingSourceCreate):
    db_obj = models.RankingSource(**ranking_source.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_ranking_source(db: Session, ranking_source_id: int, ranking_source: schemas.RankingSourceUpdate):
    db_obj = get_ranking_source(db, ranking_source_id)
    if db_obj:
        update_data = ranking_source.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_ranking_source(db: Session, ranking_source_id: int):
    db_obj = get_ranking_source(db, ranking_source_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
