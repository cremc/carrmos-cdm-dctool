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

# CountryGroup
class CountryGroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class CountryGroupCreate(CountryGroupBase, AuditMixinCreate):
    pass

class CountryGroupUpdate(CountryGroupBase):
    pass

class CountryGroup(CountryGroupBase, AuditMixin):
    country_group_id: int

    class Config:
        orm_mode = True

# Country
class CountryBase(BaseModel):
    name: str
    region: Optional[str] = None
    continent: Optional[str] = None
    country_dialing_code: Optional[str] = None

class CountryCreate(CountryBase, AuditMixinCreate):
    pass

class CountryUpdate(CountryBase):
    pass

class Country(CountryBase, AuditMixin):
    country_id: int

    class Config:
        orm_mode = True

# ProvinceOrState
class ProvinceOrStateBase(BaseModel):
    name: str
    description: Optional[str] = None
    country_id: int

class ProvinceOrStateCreate(ProvinceOrStateBase, AuditMixinCreate):
    pass

class ProvinceOrStateUpdate(ProvinceOrStateBase):
    pass

class ProvinceOrState(ProvinceOrStateBase, AuditMixin):
    province_or_state_id: int

    class Config:
        orm_mode = True

# City
class CityBase(BaseModel):
    name: str
    description: Optional[str] = None
    province_or_state_id: int
    google_map_url: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class CityCreate(CityBase, AuditMixinCreate):
    pass

class CityUpdate(CityBase):
    pass

class City(CityBase, AuditMixin):
    city_id: int

    class Config:
        orm_mode = True

# CountryCountryGroup (Relationship)
class CountryCountryGroupBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    country_id: int
    country_group_id: int

class CountryCountryGroupCreate(CountryCountryGroupBase, AuditMixinCreate):
    pass

class CountryCountryGroupUpdate(CountryCountryGroupBase):
    pass

class CountryCountryGroup(CountryCountryGroupBase, AuditMixin):
    country_country_group_id: int

    class Config:
        orm_mode = True

# Location
class LocationBase(BaseModel):
    location_name: str
    location_description: Optional[str] = None
    location_type: Optional[str] = None
    entity_id: Optional[int] = None
    entity_type: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    address_line_3: Optional[str] = None
    city_id: Optional[int] = None
    province_or_state_id: Optional[int] = None
    country_id: Optional[int] = None
    postal_code: Optional[str] = None
    location_urbanage: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    google_map_url: Optional[str] = None
    location_notes: Optional[str] = None

class LocationCreate(LocationBase, AuditMixinCreate):
    pass

class LocationUpdate(LocationBase):
    pass

class Location(LocationBase, AuditMixin):
    location_id: int

    class Config:
        orm_mode = True

# ContactDetails
class ContactDetailsBase(BaseModel):
    description: Optional[str] = None
    isd_code: Optional[str] = None
    phone_area_code: Optional[str] = None
    phone_number1: Optional[str] = None
    phone_type1: Optional[str] = None
    phone_number2: Optional[str] = None
    phone_type2: Optional[str] = None
    contact_hours: Optional[str] = None
    time_zone_id: Optional[int] = None
    working_days: Optional[str] = None
    email1: Optional[str] = None
    email_type1: Optional[str] = None
    email2: Optional[str] = None
    email_type2: Optional[str] = None
    email3: Optional[str] = None
    email_type3: Optional[str] = None
    email4: Optional[str] = None
    email_type4: Optional[str] = None
    url: Optional[str] = None
    linked_in_address: Optional[str] = None
    github_address: Optional[str] = None
    facebook_page: Optional[str] = None
    instagram_page: Optional[str] = None
    contact_notes: Optional[str] = None

class ContactDetailsCreate(ContactDetailsBase, AuditMixinCreate):
    pass

class ContactDetailsUpdate(ContactDetailsBase):
    pass

class ContactDetails(ContactDetailsBase, AuditMixin):
    contact_details_id: int

    class Config:
        orm_mode = True
