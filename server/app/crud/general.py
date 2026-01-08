from sqlalchemy.orm import Session
from ..models import general as models
from ..schemas import general as schemas

# CountryGroup
def get_country_group(db: Session, country_group_id: int):
    return db.query(models.CountryGroup).filter(models.CountryGroup.country_group_id == country_group_id).first()

def get_country_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CountryGroup).offset(skip).limit(limit).all()

def create_country_group(db: Session, country_group: schemas.CountryGroupCreate):
    db_obj = models.CountryGroup(**country_group.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_country_group(db: Session, country_group_id: int, country_group: schemas.CountryGroupUpdate):
    db_obj = get_country_group(db, country_group_id)
    if db_obj:
        update_data = country_group.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_country_group(db: Session, country_group_id: int):
    db_obj = get_country_group(db, country_group_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# Country
def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.country_id == country_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: schemas.CountryCreate):
    db_obj = models.Country(**country.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_country(db: Session, country_id: int, country: schemas.CountryUpdate):
    db_obj = get_country(db, country_id)
    if db_obj:
        update_data = country.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_country(db: Session, country_id: int):
    db_obj = get_country(db, country_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# ProvinceOrState
def get_province_or_state(db: Session, province_or_state_id: int):
    return db.query(models.ProvinceOrState).filter(models.ProvinceOrState.province_or_state_id == province_or_state_id).first()

def get_provinces_or_states(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProvinceOrState).offset(skip).limit(limit).all()

def create_province_or_state(db: Session, province_or_state: schemas.ProvinceOrStateCreate):
    db_obj = models.ProvinceOrState(**province_or_state.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_province_or_state(db: Session, province_or_state_id: int, province_or_state: schemas.ProvinceOrStateUpdate):
    db_obj = get_province_or_state(db, province_or_state_id)
    if db_obj:
        update_data = province_or_state.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_province_or_state(db: Session, province_or_state_id: int):
    db_obj = get_province_or_state(db, province_or_state_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# City
def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.city_id == city_id).first()

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()

def create_city(db: Session, city: schemas.CityCreate):
    db_obj = models.City(**city.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_city(db: Session, city_id: int, city: schemas.CityUpdate):
    db_obj = get_city(db, city_id)
    if db_obj:
        update_data = city.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_city(db: Session, city_id: int):
    db_obj = get_city(db, city_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# CountryCountryGroup
def create_country_country_group(db: Session, relationship: schemas.CountryCountryGroupCreate):
    db_obj = models.CountryCountryGroup(**relationship.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_country_country_group(db: Session, relationship_id: int):
    db_obj = db.query(models.CountryCountryGroup).filter(models.CountryCountryGroup.country_country_group_id == relationship_id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# Location
def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.location_id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

def create_location(db: Session, location: schemas.LocationCreate):
    db_obj = models.Location(**location.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_location(db: Session, location_id: int, location: schemas.LocationUpdate):
    db_obj = get_location(db, location_id)
    if db_obj:
        update_data = location.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_location(db: Session, location_id: int):
    db_obj = get_location(db, location_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

# ContactDetails
def get_contact_details(db: Session, contact_details_id: int):
    return db.query(models.ContactDetails).filter(models.ContactDetails.contact_details_id == contact_details_id).first()

def get_all_contact_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ContactDetails).offset(skip).limit(limit).all()

def create_contact_details(db: Session, contact_details: schemas.ContactDetailsCreate):
    db_obj = models.ContactDetails(**contact_details.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_contact_details(db: Session, contact_details_id: int, contact_details: schemas.ContactDetailsUpdate):
    db_obj = get_contact_details(db, contact_details_id)
    if db_obj:
        update_data = contact_details.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_contact_details(db: Session, contact_details_id: int):
    db_obj = get_contact_details(db, contact_details_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
