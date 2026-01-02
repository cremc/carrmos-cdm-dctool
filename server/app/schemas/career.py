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

# IndustrySector
class IndustrySectorBase(BaseModel):
    name: str
    description: Optional[str] = None

class IndustrySectorCreate(IndustrySectorBase, AuditMixinCreate):
    pass

class IndustrySectorUpdate(IndustrySectorBase):
    pass

class IndustrySector(IndustrySectorBase, AuditMixin):
    industry_sector_id: int

    class Config:
        orm_mode = True

# Industry
class IndustryBase(BaseModel):
    industry_name: str
    description: Optional[str] = None
    equivalent_names: Optional[str] = None
    industry_sector_id: int

class IndustryCreate(IndustryBase, AuditMixinCreate):
    pass

class IndustryUpdate(IndustryBase):
    pass

class Industry(IndustryBase, AuditMixin):
    industry_id: int

    class Config:
        orm_mode = True

# IndustryBranch
class IndustryBranchBase(BaseModel):
    name: str
    description: Optional[str] = None
    equivalent_names: Optional[str] = None
    industry_id: int

class IndustryBranchCreate(IndustryBranchBase, AuditMixinCreate):
    pass

class IndustryBranchUpdate(IndustryBranchBase):
    pass

class IndustryBranch(IndustryBranchBase, AuditMixin):
    industry_branch_id: int

    class Config:
        orm_mode = True

# CareerPosition
class CareerPositionBase(BaseModel):
    name: str
    short_description: Optional[str] = None
    long_description: Optional[str] = None
    salary_range: Optional[str] = None
    industry_branch_id: int
    industry_id: int
    prospective_employers: Optional[str] = None
    sedantariness_expected: Optional[str] = None
    physical_load_expected: Optional[str] = None
    mental_load_expected: Optional[str] = None
    analytical_load_expected: Optional[str] = None
    amount_of_travel_expected: Optional[str] = None
    amount_of_sales_effort_expected: Optional[str] = None
    salary_potential: Optional[str] = None
    lifestyle_potential: Optional[str] = None
    career_growth_potential: Optional[str] = None
    job_stability_potential: Optional[str] = None
    travel_potential: Optional[str] = None
    wlb_potential: Optional[str] = None
    settling_down_abroad_potential: Optional[str] = None
    networking_potential: Optional[str] = None
    data_source: Optional[str] = None

class CareerPositionCreate(CareerPositionBase, AuditMixinCreate):
    pass

class CareerPositionUpdate(CareerPositionBase):
    pass

class CareerPosition(CareerPositionBase, AuditMixin):
    career_position_id: int

    class Config:
        orm_mode = True

# SkillCategory
class SkillCategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class SkillCategoryCreate(SkillCategoryBase, AuditMixinCreate):
    pass

class SkillCategoryUpdate(SkillCategoryBase):
    pass

class SkillCategory(SkillCategoryBase, AuditMixin):
    skill_category_id: int

    class Config:
        orm_mode = True

# SkillSubcategory
class SkillSubcategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    skill_category_id: int
    skill_class: Optional[str] = None
    can_be_a_vocation: Optional[str] = None

class SkillSubcategoryCreate(SkillSubcategoryBase, AuditMixinCreate):
    pass

class SkillSubcategoryUpdate(SkillSubcategoryBase):
    pass

class SkillSubcategory(SkillSubcategoryBase, AuditMixin):
    skill_subcategory_id: int

    class Config:
        orm_mode = True

# ScoreReference
class ScoreReferenceBase(BaseModel):
    name: str
    description: Optional[str] = None
    score_min_value: Optional[float] = None
    score_max_value: Optional[float] = None
    score_min_max_type: Optional[str] = None
    range1: Optional[str] = None
    range2: Optional[str] = None
    range3: Optional[str] = None
    range4: Optional[str] = None
    range5: Optional[str] = None
    level1: Optional[str] = None
    level2: Optional[str] = None
    level3: Optional[str] = None

class ScoreReferenceCreate(ScoreReferenceBase, AuditMixinCreate):
    pass

class ScoreReferenceUpdate(ScoreReferenceBase):
    pass

class ScoreReference(ScoreReferenceBase, AuditMixin):
    score_reference_id: int

    class Config:
        orm_mode = True

# SkillSubcategoryCareerPosition (Relationship with attributes)
class SkillSubcategoryCareerPositionBase(BaseModel):
    skill_subcategory_id: int
    career_position_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    score_reference_id: Optional[int] = None
    skill_level: Optional[str] = None

class SkillSubcategoryCareerPositionCreate(SkillSubcategoryCareerPositionBase, AuditMixinCreate):
    pass

class SkillSubcategoryCareerPositionUpdate(SkillSubcategoryCareerPositionBase):
    pass

class SkillSubcategoryCareerPosition(SkillSubcategoryCareerPositionBase, AuditMixin):
    skill_subcategory_career_position_id: int

    class Config:
        orm_mode = True
