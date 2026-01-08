from sqlalchemy.orm import Session
from ..models import finance as models
from ..schemas import finance as schemas

# ExpenseType
def get_expense_type(db: Session, expense_type_id: int):
    return db.query(models.ExpenseType).filter(models.ExpenseType.expense_type_id == expense_type_id).first()

def get_expense_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ExpenseType).offset(skip).limit(limit).all()

def create_expense_type(db: Session, expense_type: schemas.ExpenseTypeCreate):
    db_obj = models.ExpenseType(**expense_type.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_expense_type(db: Session, expense_type_id: int, expense_type: schemas.ExpenseTypeUpdate):
    db_obj = get_expense_type(db, expense_type_id)
    if db_obj:
        update_data = expense_type.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_expense_type(db: Session, expense_type_id: int):
    db_obj = get_expense_type(db, expense_type_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# FinancialAidType
def get_financial_aid_type(db: Session, financial_aid_type_id: int):
    return db.query(models.FinancialAidType).filter(models.FinancialAidType.financial_aid_type_id == financial_aid_type_id).first()

def get_financial_aid_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FinancialAidType).offset(skip).limit(limit).all()

def create_financial_aid_type(db: Session, financial_aid_type: schemas.FinancialAidTypeCreate):
    db_obj = models.FinancialAidType(**financial_aid_type.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_financial_aid_type(db: Session, financial_aid_type_id: int, financial_aid_type: schemas.FinancialAidTypeUpdate):
    db_obj = get_financial_aid_type(db, financial_aid_type_id)
    if db_obj:
        update_data = financial_aid_type.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_financial_aid_type(db: Session, financial_aid_type_id: int):
    db_obj = get_financial_aid_type(db, financial_aid_type_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# Currency
def get_currency(db: Session, currency_id: int):
    return db.query(models.Currency).filter(models.Currency.currency_id == currency_id).first()

def get_currencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Currency).offset(skip).limit(limit).all()

def create_currency(db: Session, currency: schemas.CurrencyCreate):
    db_obj = models.Currency(**currency.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_currency(db: Session, currency_id: int, currency: schemas.CurrencyUpdate):
    db_obj = get_currency(db, currency_id)
    if db_obj:
        update_data = currency.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_currency(db: Session, currency_id: int):
    db_obj = get_currency(db, currency_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
