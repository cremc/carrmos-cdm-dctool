from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class RankingSource(Base, AuditMixin):
    __tablename__ = "ranking_source"

    ranking_source_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    year_of_survey = Column(Integer)
    target_type = Column(String(100))
    target_name = Column(String(255))
    target_id = Column(Integer)
    country_id = Column(Integer) # FK to Country
    year_established = Column(Integer)
    ranking_type = Column(String(100))
