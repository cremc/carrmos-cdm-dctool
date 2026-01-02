from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class AuditMixinBase(BaseModel):
    pass

class AuditMixinCreate(AuditMixinBase):
    created_by: Optional[str] = "system"
    updated_by: Optional[str] = "system"

class AuditMixin(AuditMixinBase):
    created_by: Optional[str]
    created_date: Optional[datetime]
    updated_by: Optional[str]
    updated_date: Optional[datetime]

# DisciplineIndustryBranch
class DisciplineIndustryBranchBase(BaseModel):
    discipline_id: int
    industry_branch_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    is_main_stream_discipline_branch: Optional[bool] = None

class DisciplineIndustryBranchCreate(DisciplineIndustryBranchBase, AuditMixinCreate):
    pass

class DisciplineIndustryBranchUpdate(DisciplineIndustryBranchBase):
    pass

class DisciplineIndustryBranch(DisciplineIndustryBranchBase, AuditMixin):
    discipline_industry_branch_id: int

    class Config:
        orm_mode = True
