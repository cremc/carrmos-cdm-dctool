from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import finance as schemas
from ..crud import finance as crud

router = APIRouter(
    prefix="/finance",
    tags=["finance"],
    responses={404: {"description": "Not found"}},
)

# ExpenseType
@router.post("/expense_types/", response_model=schemas.ExpenseType)
def create_expense_type(expense_type: schemas.ExpenseTypeCreate, db: Session = Depends(get_db)):
    return crud.create_expense_type(db=db, expense_type=expense_type)

@router.get("/expense_types/", response_model=List[schemas.ExpenseType])
def read_expense_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_expense_types(db, skip=skip, limit=limit)

@router.get("/expense_types/{expense_type_id}", response_model=schemas.ExpenseType)
def read_expense_type(expense_type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_expense_type(db, expense_type_id=expense_type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expense Type not found")
    return db_obj

@router.put("/expense_types/{expense_type_id}", response_model=schemas.ExpenseType)
def update_expense_type(expense_type_id: int, expense_type: schemas.ExpenseTypeUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_expense_type(db, expense_type_id=expense_type_id, expense_type=expense_type)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expense Type not found")
    return db_obj

@router.delete("/expense_types/{expense_type_id}", response_model=schemas.ExpenseType)
def delete_expense_type(expense_type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_expense_type(db, expense_type_id=expense_type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expense Type not found")
    return db_obj

# FinancialAidType
@router.post("/financial_aid_types/", response_model=schemas.FinancialAidType)
def create_financial_aid_type(financial_aid_type: schemas.FinancialAidTypeCreate, db: Session = Depends(get_db)):
    return crud.create_financial_aid_type(db=db, financial_aid_type=financial_aid_type)

@router.get("/financial_aid_types/", response_model=List[schemas.FinancialAidType])
def read_financial_aid_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_financial_aid_types(db, skip=skip, limit=limit)

@router.get("/financial_aid_types/{financial_aid_type_id}", response_model=schemas.FinancialAidType)
def read_financial_aid_type(financial_aid_type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_financial_aid_type(db, financial_aid_type_id=financial_aid_type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Financial Aid Type not found")
    return db_obj

@router.put("/financial_aid_types/{financial_aid_type_id}", response_model=schemas.FinancialAidType)
def update_financial_aid_type(financial_aid_type_id: int, financial_aid_type: schemas.FinancialAidTypeUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_financial_aid_type(db, financial_aid_type_id=financial_aid_type_id, financial_aid_type=financial_aid_type)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Financial Aid Type not found")
    return db_obj

@router.delete("/financial_aid_types/{financial_aid_type_id}", response_model=schemas.FinancialAidType)
def delete_financial_aid_type(financial_aid_type_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_financial_aid_type(db, financial_aid_type_id=financial_aid_type_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Financial Aid Type not found")
    return db_obj

# Currency
@router.post("/currencies/", response_model=schemas.Currency)
def create_currency(currency: schemas.CurrencyCreate, db: Session = Depends(get_db)):
    return crud.create_currency(db=db, currency=currency)

@router.get("/currencies/", response_model=List[schemas.Currency])
def read_currencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_currencies(db, skip=skip, limit=limit)

@router.get("/currencies/{currency_id}", response_model=schemas.Currency)
def read_currency(currency_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_currency(db, currency_id=currency_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_obj

@router.put("/currencies/{currency_id}", response_model=schemas.Currency)
def update_currency(currency_id: int, currency: schemas.CurrencyUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_currency(db, currency_id=currency_id, currency=currency)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_obj

@router.delete("/currencies/{currency_id}", response_model=schemas.Currency)
def delete_currency(currency_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_currency(db, currency_id=currency_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_obj
