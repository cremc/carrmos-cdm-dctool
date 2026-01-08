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

# TargetStudentType
class TargetStudentTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class TargetStudentTypeCreate(TargetStudentTypeBase, AuditMixinCreate):
    pass

class TargetStudentTypeUpdate(TargetStudentTypeBase):
    pass

class TargetStudentType(TargetStudentTypeBase, AuditMixin):
    target_student_type_id: int

    class Config:
        orm_mode = True

# AttendanceType
class AttendanceTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class AttendanceTypeCreate(AttendanceTypeBase, AuditMixinCreate):
    pass

class AttendanceTypeUpdate(AttendanceTypeBase):
    pass

class AttendanceType(AttendanceTypeBase, AuditMixin):
    attendance_type_id: int

    class Config:
        orm_mode = True

# CourseSpecific
class CourseSpecificBase(BaseModel):
    name: str
    description: Optional[str] = None
    institution_id: Optional[int] = None
    course_general_id: Optional[int] = None
    admission_criteria_description: Optional[str] = None
    AAA__ID: Optional[int] = None
    course_type: Optional[str] = None
    course_tuition_cost_INR: Optional[float] = None
    degree_or_certificate_awarded: Optional[str] = None
    certified_by_institution_id: Optional[int] = None
    conducted_by_institution_id: Optional[int] = None
    course_duration_days: Optional[int] = None
    course_duration_weeks: Optional[int] = None
    course_duration_months: Optional[float] = None
    course_duration_academic_sessions: Optional[float] = None
    course_preparation_advice: Optional[str] = None
    course_description_for_rigour: Optional[str] = None
    activeness_expected: Optional[str] = None
    physical_load_expected: Optional[str] = None
    mental_load_expected: Optional[str] = None
    analytical_load_expected: Optional[str] = None

class CourseSpecificCreate(CourseSpecificBase, AuditMixinCreate):
    pass

class CourseSpecificUpdate(CourseSpecificBase):
    pass

class CourseSpecific(CourseSpecificBase, AuditMixin):
    course_specific_id: int

    class Config:
        orm_mode = True

# CourseSpecificTargetStudentType
class CourseSpecificTargetStudentTypeBase(BaseModel):
    course_specific_id: int
    target_student_type_id: int

class CourseSpecificTargetStudentTypeCreate(CourseSpecificTargetStudentTypeBase, AuditMixinCreate):
    pass

class CourseSpecificTargetStudentTypeUpdate(CourseSpecificTargetStudentTypeBase):
    pass

class CourseSpecificTargetStudentType(CourseSpecificTargetStudentTypeBase, AuditMixin):
    course_specific_target_student_type_id: int

    class Config:
        orm_mode = True

# CourseSpecificAttendanceType
class CourseSpecificAttendanceTypeBase(BaseModel):
    course_specific_id: int
    attendance_type_id: int

class CourseSpecificAttendanceTypeCreate(CourseSpecificAttendanceTypeBase, AuditMixinCreate):
    pass

class CourseSpecificAttendanceTypeUpdate(CourseSpecificAttendanceTypeBase):
    pass

class CourseSpecificAttendanceType(CourseSpecificAttendanceTypeBase, AuditMixin):
    course_specific_attendance_type_id: int

    class Config:
        orm_mode = True

# CourseSpecificRanking
class CourseSpecificRankingBase(BaseModel):
    course_specific_id: int
    rank: Optional[int] = None
    year_of_rank: Optional[int] = None
    description: Optional[str] = None
    ranking_source_id: Optional[int] = None

class CourseSpecificRankingCreate(CourseSpecificRankingBase, AuditMixinCreate):
    pass

class CourseSpecificRankingUpdate(CourseSpecificRankingBase):
    pass

class CourseSpecificRanking(CourseSpecificRankingBase, AuditMixin):
    course_specific_ranking_id: int

    class Config:
        orm_mode = True

# CourseSpecificExpense
class CourseSpecificExpenseBase(BaseModel):
    name: str
    description: Optional[str] = None
    course_specific_id: int
    expense_type_id: Optional[int] = None
    frequency: Optional[str] = None
    currency_id: Optional[int] = None
    amount: Optional[float] = None

class CourseSpecificExpenseCreate(CourseSpecificExpenseBase, AuditMixinCreate):
    pass

class CourseSpecificExpenseUpdate(CourseSpecificExpenseBase):
    pass

class CourseSpecificExpense(CourseSpecificExpenseBase, AuditMixin):
    course_specific_expense_id: int

    class Config:
        orm_mode = True
