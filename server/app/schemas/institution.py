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

# Institution
class InstitutionBase(BaseModel):
    name: str
    short_description: Optional[str] = None
    long_description: Optional[str] = None
    popular_names: Optional[str] = None
    parent_institution_id: Optional[int] = None
    year_established: Optional[int] = None
    url: Optional[str] = None
    location: Optional[str] = None

class InstitutionCreate(InstitutionBase, AuditMixinCreate):
    pass

class InstitutionUpdate(InstitutionBase):
    pass

class Institution(InstitutionBase, AuditMixin):
    institution_id: int

    class Config:
        orm_mode = True

# InstitutionCategory
class InstitutionCategoryBase(BaseModel):
    name: str
    popular_name: Optional[str] = None
    description: Optional[str] = None
    country_id: Optional[int] = None

class InstitutionCategoryCreate(InstitutionCategoryBase, AuditMixinCreate):
    pass

class InstitutionCategoryUpdate(InstitutionCategoryBase):
    pass

class InstitutionCategory(InstitutionCategoryBase, AuditMixin):
    institution_category_id: int

    class Config:
        orm_mode = True

# AssociationAccreditationAffiliation (AAA)
class AAABase(BaseModel):
    name: str
    description: Optional[str] = None
    aaa_type: Optional[str] = None
    country_id: Optional[int] = None

class AAACreate(AAABase, AuditMixinCreate):
    pass

class AAAUpdate(AAABase):
    pass

class AAA(AAABase, AuditMixin):
    aaa_id: int

    class Config:
        orm_mode = True
