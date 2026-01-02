from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class CourseSpecific(Base, AuditMixin):
    __tablename__ = "course_specific"

    course_specific_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    institution_id = Column(Integer) # FK to Institution
    course_general_id = Column(Integer) # FK to CourseGeneral
    admission_criteria_description = Column(Text)
    AAA__ID = Column(Integer) # FK to AAA
    course_type = Column(String(255))
    course_tuition_cost_INR = Column(Float)
    degree_or_certificate_awarded = Column(String(255))
    certified_by_institution_id = Column(Integer)
    conducted_by_institution_id = Column(Integer)
    course_duration_days = Column(Integer)
    course_duration_weeks = Column(Integer)
    course_duration_months = Column(Float)
    course_duration_academic_sessions = Column(Float)
    course_preparation_advice = Column(Text)
    course_description_for_rigour = Column(Text)
    activeness_expected = Column(String(100))
    physical_load_expected = Column(String(100))
    mental_load_expected = Column(String(100))
    analytical_load_expected = Column(String(100))

class TargetStudentType(Base, AuditMixin):
    __tablename__ = "target_student_type"

    target_student_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class AttendanceType(Base, AuditMixin):
    __tablename__ = "attendance_type"

    attendance_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class CourseSpecificTargetStudentType(Base, AuditMixin):
    __tablename__ = "course_specific_target_student_type"

    course_specific_target_student_type_id = Column(Integer, primary_key=True, index=True)
    course_specific_id = Column(Integer, ForeignKey("course_specific.course_specific_id"))
    target_student_type_id = Column(Integer, ForeignKey("target_student_type.target_student_type_id"))

class CourseSpecificAttendanceType(Base, AuditMixin):
    __tablename__ = "course_specific_attendance_type"

    course_specific_attendance_type_id = Column(Integer, primary_key=True, index=True)
    course_specific_id = Column(Integer, ForeignKey("course_specific.course_specific_id"))
    attendance_type_id = Column(Integer, ForeignKey("attendance_type.attendance_type_id"))

class CourseSpecificRanking(Base, AuditMixin):
    __tablename__ = "course_specific_ranking"

    course_specific_ranking_id = Column(Integer, primary_key=True, index=True)
    course_specific_id = Column(Integer, ForeignKey("course_specific.course_specific_id"))
    rank = Column(Integer)
    year_of_rank = Column(Integer)
    description = Column(Text)
    ranking_source_id = Column(Integer) # FK to RankingSource

class CourseSpecificExpense(Base, AuditMixin):
    __tablename__ = "course_specific_expense"

    course_specific_expense_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    course_specific_id = Column(Integer, ForeignKey("course_specific.course_specific_id"))
    expense_type_id = Column(Integer) # FK to Finance
    frequency = Column(String(100))
    currency_id = Column(Integer) # FK to Finance
    amount = Column(Float)
