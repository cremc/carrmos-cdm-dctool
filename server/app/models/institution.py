from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class Institution(Base, AuditMixin):
    __tablename__ = "institution"

    institution_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    short_description = Column(Text)
    long_description = Column(Text)
    popular_names = Column(Text)
    parent_institution_id = Column(Integer, ForeignKey("institution.institution_id"), nullable=True)
    year_established = Column(Integer)
    url = Column(String(255))
    location = Column(Text) # Might need to link to Location table later, currently text

    parent_institution = relationship("Institution", remote_side=[institution_id])

class InstitutionCategory(Base, AuditMixin):
    __tablename__ = "institution_category"

    institution_category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    popular_name = Column(String(255))
    description = Column(Text)
    country_id = Column(Integer) # FK to Country

class AssociationAccreditationAffiliation(Base, AuditMixin):
    __tablename__ = "association_accreditation_affiliation"

    aaa_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    aaa_type_id = Column(Integer)
    country_id = Column(Integer) # FK to Country
