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

# ExpenseType
class ExpenseTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class ExpenseTypeCreate(ExpenseTypeBase, AuditMixinCreate):
    pass

class ExpenseTypeUpdate(ExpenseTypeBase):
    pass

class ExpenseType(ExpenseTypeBase, AuditMixin):
    expense_type_id: int

    class Config:
        orm_mode = True

# FinancialAidType
class FinancialAidTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class FinancialAidTypeCreate(FinancialAidTypeBase, AuditMixinCreate):
    pass

class FinancialAidTypeUpdate(FinancialAidTypeBase):
    pass

class FinancialAidType(FinancialAidTypeBase, AuditMixin):
    financial_aid_type_id: int

    class Config:
        orm_mode = True

# Currency
class CurrencyBase(BaseModel):
    name: str
    description: Optional[str] = None
    currency_code: Optional[str] = None
    country_id: Optional[int] = None

class CurrencyCreate(CurrencyBase, AuditMixinCreate):
    pass

class CurrencyUpdate(CurrencyBase):
    pass

class Currency(CurrencyBase, AuditMixin):
    currency_id: int

    class Config:
        orm_mode = True
