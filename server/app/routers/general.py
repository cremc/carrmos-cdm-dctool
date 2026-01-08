from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import general as schemas
from ..crud import general as crud

router = APIRouter(
    prefix="/general",
    tags=["general"],
    responses={404: {"description": "Not found"}},
)

# CountryGroup
@router.post("/country_groups/", response_model=schemas.CountryGroup)
def create_country_group(country_group: schemas.CountryGroupCreate, db: Session = Depends(get_db)):
    return crud.create_country_group(db=db, country_group=country_group)

@router.get("/country_groups/", response_model=List[schemas.CountryGroup])
def read_country_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_country_groups(db, skip=skip, limit=limit)

@router.get("/country_groups/{country_group_id}", response_model=schemas.CountryGroup)
def read_country_group(country_group_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_country_group(db, country_group_id=country_group_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Country Group not found")
    return db_obj

@router.put("/country_groups/{country_group_id}", response_model=schemas.CountryGroup)
def update_country_group(country_group_id: int, country_group: schemas.CountryGroupUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_country_group(db, country_group_id=country_group_id, country_group=country_group)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Country Group not found")
    return db_obj

@router.delete("/country_groups/{country_group_id}", response_model=schemas.CountryGroup)
def delete_country_group(country_group_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_country_group(db, country_group_id=country_group_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Country Group not found")
    return db_obj

# Country
@router.post("/countries/", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)

@router.get("/countries/", response_model=List[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_countries(db, skip=skip, limit=limit)

@router.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_country(db, country_id=country_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_obj

@router.put("/countries/{country_id}", response_model=schemas.Country)
def update_country(country_id: int, country: schemas.CountryUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_country(db, country_id=country_id, country=country)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_obj

@router.delete("/countries/{country_id}", response_model=schemas.Country)
def delete_country(country_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_country(db, country_id=country_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_obj

# ProvinceOrState
@router.post("/provinces/", response_model=schemas.ProvinceOrState)
def create_province_or_state(province_or_state: schemas.ProvinceOrStateCreate, db: Session = Depends(get_db)):
    return crud.create_province_or_state(db=db, province_or_state=province_or_state)

@router.get("/provinces/", response_model=List[schemas.ProvinceOrState])
def read_provinces_or_states(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_provinces_or_states(db, skip=skip, limit=limit)

@router.get("/provinces/{province_or_state_id}", response_model=schemas.ProvinceOrState)
def read_province_or_state(province_or_state_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_province_or_state(db, province_or_state_id=province_or_state_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Province/State not found")
    return db_obj

@router.put("/provinces/{province_or_state_id}", response_model=schemas.ProvinceOrState)
def update_province_or_state(province_or_state_id: int, province_or_state: schemas.ProvinceOrStateUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_province_or_state(db, province_or_state_id=province_or_state_id, province_or_state=province_or_state)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Province/State not found")
    return db_obj

@router.delete("/provinces/{province_or_state_id}", response_model=schemas.ProvinceOrState)
def delete_province_or_state(province_or_state_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_province_or_state(db, province_or_state_id=province_or_state_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Province/State not found")
    return db_obj

# City
@router.post("/cities/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db=db, city=city)

@router.get("/cities/", response_model=List[schemas.City])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cities(db, skip=skip, limit=limit)

@router.get("/cities/{city_id}", response_model=schemas.City)
def read_city(city_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_city(db, city_id=city_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="City not found")
    return db_obj

@router.put("/cities/{city_id}", response_model=schemas.City)
def update_city(city_id: int, city: schemas.CityUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_city(db, city_id=city_id, city=city)
    if not db_obj:
        raise HTTPException(status_code=404, detail="City not found")
    return db_obj

@router.delete("/cities/{city_id}", response_model=schemas.City)
def delete_city(city_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_city(db, city_id=city_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="City not found")
    return db_obj

# CountryCountryGroup (Relationship)
@router.post("/country_groups/members/", response_model=schemas.CountryCountryGroup)
def create_country_country_group(relationship: schemas.CountryCountryGroupCreate, db: Session = Depends(get_db)):
    return crud.create_country_country_group(db=db, relationship=relationship)

@router.delete("/country_groups/members/{relationship_id}", response_model=schemas.CountryCountryGroup)
def delete_country_country_group(relationship_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_country_country_group(db, relationship_id=relationship_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return db_obj

# Location
@router.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)

@router.get("/locations/", response_model=List[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_locations(db, skip=skip, limit=limit)

@router.get("/locations/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_location(db, location_id=location_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_obj

@router.put("/locations/{location_id}", response_model=schemas.Location)
def update_location(location_id: int, location: schemas.LocationUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_location(db, location_id=location_id, location=location)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_obj

@router.delete("/locations/{location_id}", response_model=schemas.Location)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_location(db, location_id=location_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_obj

# ContactDetails
@router.post("/contact_details/", response_model=schemas.ContactDetails)
def create_contact_details(contact_details: schemas.ContactDetailsCreate, db: Session = Depends(get_db)):
    return crud.create_contact_details(db=db, contact_details=contact_details)

@router.get("/contact_details/", response_model=List[schemas.ContactDetails])
def read_all_contact_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_contact_details(db, skip=skip, limit=limit)

@router.get("/contact_details/{contact_details_id}", response_model=schemas.ContactDetails)
def read_contact_details(contact_details_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_contact_details(db, contact_details_id=contact_details_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Contact Details not found")
    return db_obj

@router.put("/contact_details/{contact_details_id}", response_model=schemas.ContactDetails)
def update_contact_details(contact_details_id: int, contact_details: schemas.ContactDetailsUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_contact_details(db, contact_details_id=contact_details_id, contact_details=contact_details)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Contact Details not found")
    return db_obj

@router.delete("/contact_details/{contact_details_id}", response_model=schemas.ContactDetails)
def delete_contact_details(contact_details_id: int, db: Session = Depends(get_db)):
    db_obj = crud.delete_contact_details(db, contact_details_id=contact_details_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Contact Details not found")
    return db_obj
