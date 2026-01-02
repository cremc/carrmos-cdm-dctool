from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class GroupingReference(Base, AuditMixin):
    __tablename__ = "grouping_reference"

    requirement_group_id = Column(Integer, primary_key=True, index=True)
    Grouping_for = Column(String(255))
    Milestone_type = Column(String(255))
    Academic_Requirement_ID = Column(Integer)

class MilestoneAcademicRequirement(Base, AuditMixin):
    __tablename__ = "milestone_academic_requirement"

    milestone_academic_requirement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    calling_milestone_id = Column(Integer)
    calling_milestone_type = Column(String(255))
    prerequisite_academic_level_id = Column(Integer)
    prerequisite_course_general_id = Column(Integer)
    prerequisite_stream_id = Column(Integer)
    prerequisite_discipline_group_id = Column(Integer)
    prerequisite_discipline_id = Column(Integer)
    prerequisite_score_reference_id = Column(Integer)
    prerequisite_score_value_min = Column(Float)
    requirement_group_id = Column(Integer, ForeignKey("grouping_reference.requirement_group_id"))

class MilestoneWorkexRequirement(Base, AuditMixin):
    __tablename__ = "milestone_workex_requirement"

    milestone_workex_requirement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    calling_milestone_id = Column(Integer)
    calling_milestone_type = Column(String(255))
    prerequisite_career_position_id = Column(Integer)
    prerequisite_industry_id = Column(Integer)
    prerequisite_industry_branch_id = Column(Integer)
    prerequisite_workex_min_duration_yrs = Column(Float)
    requirement_group_id = Column(Integer, ForeignKey("grouping_reference.requirement_group_id"))
    dependency_type = Column(String(100))

class MilestoneSkillRequirement(Base, AuditMixin):
    __tablename__ = "milestone_skill_requirement"

    milestone_skill_requirement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    calling_milestone_id = Column(Integer)
    calling_milestone_type = Column(String(255))
    prerequisite_skill_category_id = Column(Integer)
    prerequisite_skill_subcategory_id = Column(Integer)
    score_reference_id = Column(Integer)
    prerequisite_skill_level = Column(String(100))
    requirement_group_id = Column(Integer, ForeignKey("grouping_reference.requirement_group_id"))
    dependency_type = Column(String(100))

class MilestoneEntranceRequirement(Base, AuditMixin):
    __tablename__ = "milestone_entrance_requirement"

    milestone_entrance_requirement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    calling_milestone_id = Column(Integer)
    calling_milestone_type = Column(String(255))
    prerequisite_entrance_test_id = Column(Integer)
    prerequisite_score_value_min = Column(Float)
    requirement_group_id = Column(Integer, ForeignKey("grouping_reference.requirement_group_id"))
    dependency_type = Column(String(100))

class MilestoneCertificationRequirement(Base, AuditMixin):
    __tablename__ = "milestone_certification_requirement"

    milestone_certification_requirement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    calling_milestone_id = Column(Integer)
    calling_milestone_type = Column(String(255))
    prerequisite_certification_id = Column(Integer) # course_specific_id
    prerequisite_score_value_min = Column(Float)
    requirement_group_id = Column(Integer, ForeignKey("grouping_reference.requirement_group_id"))
    dependency_type = Column(String(100))

class MilestoneOtherRequirement(Base, AuditMixin):
    __tablename__ = "milestone_other_requirement"

    milestone_other_requirement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    calling_milestone_id = Column(Integer)
    calling_milestone_type = Column(String(255))
    prerequisite_description = Column(Text)
    dependency_type = Column(String(100))
