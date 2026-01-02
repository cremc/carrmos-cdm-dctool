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

# AcademicLevel
class AcademicLevelBase(BaseModel):
    name: str
    description: Optional[str] = None
    min_years_to_complete: Optional[float] = None
    average_years_to_complete: Optional[float] = None
    max_years_to_complete: Optional[float] = None
    prerequisite_academic_level_ID: Optional[int] = None
    order: Optional[int] = None

class AcademicLevelCreate(AcademicLevelBase, AuditMixinCreate):
    pass

class AcademicLevelUpdate(AcademicLevelBase):
    pass

class AcademicLevel(AcademicLevelBase, AuditMixin):
    academic_level_id: int

    class Config:
        orm_mode = True

# Stream
class StreamBase(BaseModel):
    name: str
    description: Optional[str] = None
    equivalent_names: Optional[str] = None
    parent_stream_id: Optional[int] = None

class StreamCreate(StreamBase, AuditMixinCreate):
    pass

class StreamUpdate(StreamBase):
    pass

class Stream(StreamBase, AuditMixin):
    stream_id: int

    class Config:
        orm_mode = True

# DisciplineGroup
class DisciplineGroupBase(BaseModel):
    name: str
    description: Optional[str] = None
    stream_id: int

class DisciplineGroupCreate(DisciplineGroupBase, AuditMixinCreate):
    pass

class DisciplineGroupUpdate(DisciplineGroupBase):
    pass

class DisciplineGroup(DisciplineGroupBase, AuditMixin):
    discipline_group_id: int

    class Config:
        orm_mode = True

# Discipline
class DisciplineBase(BaseModel):
    name: str
    description: Optional[str] = None
    discipline_group_id: int

class DisciplineCreate(DisciplineBase, AuditMixinCreate):
    pass

class DisciplineUpdate(DisciplineBase):
    pass

class Discipline(DisciplineBase, AuditMixin):
    discipline_id: int

    class Config:
        orm_mode = True

# CourseGeneral
class CourseGeneralBase(BaseModel):
    academic_level_id: int
    name: str
    description: Optional[str] = None
    course_alternate_names: Optional[str] = None
    course_type: Optional[str] = None
    course_duration_months: Optional[float] = None
    course_description_for_rigour: Optional[str] = None
    course_tuition_cost_inr: Optional[float] = None
    course_description_for_career: Optional[str] = None

class CourseGeneralCreate(CourseGeneralBase, AuditMixinCreate):
    pass

class CourseGeneralUpdate(CourseGeneralBase):
    pass

class CourseGeneral(CourseGeneralBase, AuditMixin):
    course_general_id: int

    class Config:
        orm_mode = True

# CoreSubject
class CoreSubjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class CoreSubjectCreate(CoreSubjectBase, AuditMixinCreate):
    pass

class CoreSubjectUpdate(CoreSubjectBase):
    pass

class CoreSubject(CoreSubjectBase, AuditMixin):
    core_subject_id: int

    class Config:
        orm_mode = True

# CourseGeneralCoreSubject (Relationship)
class CourseGeneralCoreSubjectBase(BaseModel):
    course_general_id: int
    core_subject_id: int

class CourseGeneralCoreSubjectCreate(CourseGeneralCoreSubjectBase, AuditMixinCreate):
    pass

class CourseGeneralCoreSubject(CourseGeneralCoreSubjectBase, AuditMixin):
    course_general_core_subject_id: int

    class Config:
        orm_mode = True

# CourseGeneralDiscipline (Relationship)
class CourseGeneralDisciplineBase(BaseModel):
    course_general_id: int
    discipline_id: int
    discipline_group_id: int

class CourseGeneralDisciplineCreate(CourseGeneralDisciplineBase, AuditMixinCreate):
    pass

class CourseGeneralDiscipline(CourseGeneralDisciplineBase, AuditMixin):
    course_general_discipline_id: int

    class Config:
        orm_mode = True
