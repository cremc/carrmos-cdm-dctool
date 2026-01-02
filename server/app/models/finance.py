from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class ExpenseType(Base, AuditMixin):
    __tablename__ = "expense_type"

    expense_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class FinancialAidType(Base, AuditMixin):
    __tablename__ = "financial_aid_type"

    financial_aid_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class Currency(Base, AuditMixin):
    __tablename__ = "currency"

    currency_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    currency_code = Column(String(10))
    country_id = Column(Integer) # FK to Country
