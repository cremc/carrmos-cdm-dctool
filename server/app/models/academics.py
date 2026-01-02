from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class AuditMixin:
    created_by = Column(String(255))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_by = Column(String(255))
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AcademicLevel(Base, AuditMixin):
    __tablename__ = "academic_level"
    
    academic_level_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    min_years_to_complete = Column(Float)
    average_years_to_complete = Column(Float)
    max_years_to_complete = Column(Float)
    prerequisite_academic_level_ID = Column(Integer, ForeignKey("academic_level.academic_level_id"), nullable=True)
    order = Column(Integer)

    parent_level = relationship("AcademicLevel", remote_side=[academic_level_id])

class Stream(Base, AuditMixin):
    __tablename__ = "stream"

    stream_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    equivalent_names = Column(Text)
    parent_stream_id = Column(Integer, ForeignKey("stream.stream_id"), nullable=True)

    parent_stream = relationship("Stream", remote_side=[stream_id])
    discipline_groups = relationship("DisciplineGroup", back_populates="stream")

class DisciplineGroup(Base, AuditMixin):
    __tablename__ = "discipline_group"

    discipline_group_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    stream_id = Column(Integer, ForeignKey("stream.stream_id"))

    stream = relationship("Stream", back_populates="discipline_groups")
    disciplines = relationship("Discipline", back_populates="discipline_group")

class Discipline(Base, AuditMixin):
    __tablename__ = "discipline"

    discipline_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    discipline_group_id = Column(Integer, ForeignKey("discipline_group.discipline_group_id"))

    discipline_group = relationship("DisciplineGroup", back_populates="disciplines")

class CourseGeneral(Base, AuditMixin):
    __tablename__ = "course_general"

    course_general_id = Column(Integer, primary_key=True, index=True)
    academic_level_id = Column(Integer, ForeignKey("academic_level.academic_level_id"))
    name = Column(String(255))
    description = Column(Text)
    course_alternate_names = Column(Text)
    course_type = Column(String(255))
    course_duration_months = Column(Float)
    course_description_for_rigour = Column(Text)
    course_tuition_cost_inr = Column(Float)
    course_description_for_career = Column(Text)

    academic_level = relationship("AcademicLevel")

class CoreSubject(Base, AuditMixin):
    __tablename__ = "core_subject"

    core_subject_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class EntranceTest(Base, AuditMixin):
    __tablename__ = "entrance_test"

    entrance_test_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    full_name = Column(String(255))
    test_objective = Column(Text)
    test_cost_description = Column(Text)
    test_version = Column(String(100))
    test_objective_type = Column(String(100)) # Enum
    test_curriculum_description = Column(Text)
    test_rigour_description = Column(Text)
    test_preparation_advice = Column(Text)
    score_reference_id = Column(Integer) # FK to score_reference (Career domain)
    score_system_description = Column(Text)
    conducted_by_institution = Column(String(255))
    year_established = Column(Integer)
    url = Column(String(255))

class CourseGeneralCoreSubject(Base, AuditMixin):
    __tablename__ = "course_general_core_subject"

    course_general_core_subject_id = Column(Integer, primary_key=True, index=True)
    course_general_id = Column(Integer, ForeignKey("course_general.course_general_id"))
    core_subject_id = Column(Integer, ForeignKey("core_subject.core_subject_id"))

class CourseGeneralDiscipline(Base, AuditMixin):
    __tablename__ = "course_general_discipline"

    course_general_discipline_id = Column(Integer, primary_key=True, index=True)
    course_general_id = Column(Integer, ForeignKey("course_general.course_general_id"))
    discipline_id = Column(Integer, ForeignKey("discipline.discipline_id"))
    discipline_group_id = Column(Integer, ForeignKey("discipline_group.discipline_group_id"))
