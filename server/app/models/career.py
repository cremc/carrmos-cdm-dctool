from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class IndustrySector(Base, AuditMixin):
    __tablename__ = "industry_sector"

    industry_sector_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class Industry(Base, AuditMixin):
    __tablename__ = "industry"

    industry_id = Column(Integer, primary_key=True, index=True)
    industry_name = Column(String(255))
    description = Column(Text)
    equivalent_names = Column(Text)
    industry_sector_id = Column(Integer, ForeignKey("industry_sector.industry_sector_id"))

    sector = relationship("IndustrySector")

class IndustryBranch(Base, AuditMixin):
    __tablename__ = "industry_branch"

    industry_branch_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    equivalent_names = Column(Text)
    industry_id = Column(Integer, ForeignKey("industry.industry_id"))

    industry = relationship("Industry")

class CareerPosition(Base, AuditMixin):
    __tablename__ = "career_position"

    career_position_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    short_description = Column(Text)
    long_description = Column(Text)
    salary_range = Column(String(255))
    industry_branch_id = Column(Integer, ForeignKey("industry_branch.industry_branch_id"))
    industry_id = Column(Integer, ForeignKey("industry.industry_id"))
    prospective_employers = Column(Text)
    sedantariness_expected = Column(String(100))
    physical_load_expected = Column(String(100))
    mental_load_expected = Column(String(100))
    analytical_load_expected = Column(String(100))
    amount_of_travel_expected = Column(String(100))
    amount_of_sales_effort_expected = Column(String(100))
    salary_potential = Column(String(100))
    lifestyle_potential = Column(String(100))
    career_growth_potential = Column(String(100))
    job_stability_potential = Column(String(100))
    travel_potential = Column(String(100))
    wlb_potential = Column(String(100))
    settling_down_abroad_potential = Column(String(100))
    networking_potential = Column(String(100))
    data_source = Column(String(255))

    industry = relationship("Industry")
    industry_branch = relationship("IndustryBranch")

class SkillCategory(Base, AuditMixin):
    __tablename__ = "skill_category"

    skill_category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class SkillSubcategory(Base, AuditMixin):
    __tablename__ = "skill_subcategory"

    skill_subcategory_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    skill_category_id = Column(Integer, ForeignKey("skill_category.skill_category_id"))
    skill_class = Column(String(255))
    can_be_a_vocation = Column(String(10)) # Boolean-chk

    skill_category = relationship("SkillCategory")

class ScoreReference(Base, AuditMixin):
    __tablename__ = "score_reference"

    score_reference_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    score_min_value = Column(Float)
    score_max_value = Column(Float)
    score_min_max_type = Column(String(100))
    range1 = Column(String(255))
    range2 = Column(String(255))
    range3 = Column(String(255))
    range4 = Column(String(255))
    range5 = Column(String(255))
    level1 = Column(String(255))
    level2 = Column(String(255))
    level3 = Column(String(255))

class SkillSubcategoryCareerPosition(Base, AuditMixin):
    __tablename__ = "skill_subcategory_career_position"

    skill_subcategory_career_position_id = Column(Integer, primary_key=True, index=True)
    skill_subcategory_id = Column(Integer, ForeignKey("skill_subcategory.skill_subcategory_id"))
    career_position_id = Column(Integer, ForeignKey("career_position.career_position_id"))
    name = Column(String(255))
    description = Column(Text)
    score_reference_id = Column(Integer, ForeignKey("score_reference.score_reference_id"))
    skill_level = Column(String(100))
