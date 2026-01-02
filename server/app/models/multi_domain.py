from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class DisciplineIndustryBranch(Base, AuditMixin):
    __tablename__ = "discipline_industry_branch"

    discipline_industry_branch_id = Column(Integer, primary_key=True, index=True)
    discipline_id = Column(Integer, ForeignKey("discipline.discipline_id"))
    industry_branch_id = Column(Integer, ForeignKey("industry_branch.industry_branch_id"))
    name = Column(String(255))
    description = Column(Text)
    is_main_stream_discipline_branch = Column(Boolean)

class CareerPositionCoreSubject(Base, AuditMixin):
    __tablename__ = "career_position_core_subject"

    career_position_core_subject_id = Column(Integer, primary_key=True, index=True)
    core_subject_id = Column(Integer, ForeignKey("core_subject.core_subject_id"))
    career_position_id = Column(Integer, ForeignKey("career_position.career_position_id"))
    name = Column(String(255))
    description = Column(Text)

class CourseSpecificCoreSubject(Base, AuditMixin):
    __tablename__ = "course_specific_core_subject"

    course_specific_core_subject_id = Column(Integer, primary_key=True, index=True)
    course_specific_id = Column(Integer, ForeignKey("course_specific.course_specific_id"))
    core_subject_id = Column(Integer, ForeignKey("core_subject.core_subject_id"))
    taught_by_the_name = Column(String(255))

class EntranceTestProvince(Base, AuditMixin):
    __tablename__ = "entrance_test_province"

    entrance_test_province_id = Column(Integer, primary_key=True, index=True)
    entrance_test_id = Column(Integer, ForeignKey("entrance_test.entrance_test_id"))
    province_id = Column(Integer, nullable=True) # ForeignKey to ProvinceOrState
    country_id = Column(Integer) # ForeignKey to Country

class InstitutionAAA(Base, AuditMixin):
    __tablename__ = "institution_aaa"

    institution_aaa_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    institution_id = Column(Integer, ForeignKey("institution.institution_id"))
    aaa_id = Column(Integer, ForeignKey("association_accreditation_affiliation.aaa_id"))

class CourseSpecificAAA(Base, AuditMixin):
    __tablename__ = "course_specific_aaa"

    course_specific_aaa_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    course_specific_id = Column(Integer, ForeignKey("course_specific.course_specific_id"))
    aaa_id = Column(Integer, ForeignKey("association_accreditation_affiliation.aaa_id"))
