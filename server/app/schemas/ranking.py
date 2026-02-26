from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class AuditMixinBase(BaseModel):
    pass

class AuditMixinCreate(AuditMixinBase):
    created_by: Optional[int] = 1
    updated_by: Optional[int] = 1

class AuditMixin(AuditMixinBase):
    created_by: Optional[int]
    created_date: Optional[datetime]
    updated_by: Optional[int]
    updated_date: Optional[datetime]

# RankingSource
class RankingSourceBase(BaseModel):
    name: str
    description: Optional[str] = None
    year_of_survey: Optional[int] = None
    target_type: Optional[str] = None
    target_name: Optional[str] = None
    target_id: Optional[int] = None
    country_id: Optional[int] = None
    year_established: Optional[int] = None
    ranking_type: Optional[str] = None

class RankingSourceCreate(RankingSourceBase, AuditMixinCreate):
    pass

class RankingSourceUpdate(RankingSourceBase):
    pass

class RankingSource(RankingSourceBase, AuditMixin):
    ranking_source_id: int

    class Config:
        orm_mode = True
