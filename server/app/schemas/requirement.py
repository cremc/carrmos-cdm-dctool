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

# GroupingReference
class GroupingReferenceBase(BaseModel):
    Grouping_for: Optional[str] = None
    Milestone_type: Optional[str] = None
    Academic_Requirement_ID: Optional[int] = None

class GroupingReferenceCreate(GroupingReferenceBase, AuditMixinCreate):
    pass

class GroupingReferenceUpdate(GroupingReferenceBase):
    pass

class GroupingReference(GroupingReferenceBase, AuditMixin):
    requirement_group_id: int

    class Config:
        orm_mode = True

# MilestoneAcademicRequirement
class MilestoneAcademicRequirementBase(BaseModel):
    name: str
    description: Optional[str] = None
    calling_milestone_id: Optional[int] = None
    calling_milestone_type: Optional[str] = None
    prerequisite_academic_level_id: Optional[int] = None
    prerequisite_course_general_id: Optional[int] = None
    prerequisite_stream_id: Optional[int] = None
    prerequisite_discipline_group_id: Optional[int] = None
    prerequisite_discipline_id: Optional[int] = None
    prerequisite_score_reference_id: Optional[int] = None
    prerequisite_score_value_min: Optional[float] = None
    requirement_group_id: Optional[int] = None
    dependency_type: Optional[str] = None

class MilestoneAcademicRequirementCreate(MilestoneAcademicRequirementBase, AuditMixinCreate):
    pass

class MilestoneAcademicRequirementUpdate(MilestoneAcademicRequirementBase):
    pass

class MilestoneAcademicRequirement(MilestoneAcademicRequirementBase, AuditMixin):
    milestone_academic_requirement_id: int

    class Config:
        orm_mode = True

# MilestoneWorkexRequirement
class MilestoneWorkexRequirementBase(BaseModel):
    name: str
    description: Optional[str] = None
    calling_milestone_id: Optional[int] = None
    calling_milestone_type: Optional[str] = None
    prerequisite_career_position_id: Optional[int] = None
    prerequisite_industry_id: Optional[int] = None
    prerequisite_industry_branch_id: Optional[int] = None
    prerequisite_workex_min_duration_yrs: Optional[float] = None
    requirement_group_id: Optional[int] = None
    dependency_type: Optional[str] = None

class MilestoneWorkexRequirementCreate(MilestoneWorkexRequirementBase, AuditMixinCreate):
    pass

class MilestoneWorkexRequirementUpdate(MilestoneWorkexRequirementBase):
    pass

class MilestoneWorkexRequirement(MilestoneWorkexRequirementBase, AuditMixin):
    milestone_workex_requirement_id: int

    class Config:
        orm_mode = True

# MilestoneSkillRequirement
class MilestoneSkillRequirementBase(BaseModel):
    name: str
    description: Optional[str] = None
    calling_milestone_id: Optional[int] = None
    calling_milestone_type: Optional[str] = None
    prerequisite_skill_category_id: Optional[int] = None
    prerequisite_skill_subcategory_id: Optional[int] = None
    score_reference_id: Optional[int] = None
    prerequisite_skill_level: Optional[str] = None
    requirement_group_id: Optional[int] = None
    dependency_type: Optional[str] = None

class MilestoneSkillRequirementCreate(MilestoneSkillRequirementBase, AuditMixinCreate):
    pass

class MilestoneSkillRequirementUpdate(MilestoneSkillRequirementBase):
    pass

class MilestoneSkillRequirement(MilestoneSkillRequirementBase, AuditMixin):
    milestone_skill_requirement_id: int

    class Config:
        orm_mode = True

# MilestoneEntranceRequirement
class MilestoneEntranceRequirementBase(BaseModel):
    name: str
    description: Optional[str] = None
    calling_milestone_id: Optional[int] = None
    calling_milestone_type: Optional[str] = None
    prerequisite_entrance_test_id: Optional[int] = None
    prerequisite_score_value_min: Optional[float] = None
    requirement_group_id: Optional[int] = None
    dependency_type: Optional[str] = None

class MilestoneEntranceRequirementCreate(MilestoneEntranceRequirementBase, AuditMixinCreate):
    pass

class MilestoneEntranceRequirementUpdate(MilestoneEntranceRequirementBase):
    pass

class MilestoneEntranceRequirement(MilestoneEntranceRequirementBase, AuditMixin):
    milestone_entrance_requirement_id: int

    class Config:
        orm_mode = True

# MilestoneCertificationRequirement
class MilestoneCertificationRequirementBase(BaseModel):
    name: str
    description: Optional[str] = None
    calling_milestone_id: Optional[int] = None
    calling_milestone_type: Optional[str] = None
    prerequisite_certification_id: Optional[int] = None
    prerequisite_score_value_min: Optional[float] = None
    requirement_group_id: Optional[int] = None
    dependency_type: Optional[str] = None

class MilestoneCertificationRequirementCreate(MilestoneCertificationRequirementBase, AuditMixinCreate):
    pass

class MilestoneCertificationRequirementUpdate(MilestoneCertificationRequirementBase):
    pass

class MilestoneCertificationRequirement(MilestoneCertificationRequirementBase, AuditMixin):
    milestone_certification_requirement_id: int

    class Config:
        orm_mode = True

# MilestoneOtherRequirement
class MilestoneOtherRequirementBase(BaseModel):
    name: str
    description: Optional[str] = None
    calling_milestone_id: Optional[int] = None
    calling_milestone_type: Optional[str] = None
    prerequisite_description: Optional[str] = None
    dependency_type: Optional[str] = None

class MilestoneOtherRequirementCreate(MilestoneOtherRequirementBase, AuditMixinCreate):
    pass

class MilestoneOtherRequirementUpdate(MilestoneOtherRequirementBase):
    pass

class MilestoneOtherRequirement(MilestoneOtherRequirementBase, AuditMixin):
    milestone_other_requirement_id: int

    class Config:
        orm_mode = True
