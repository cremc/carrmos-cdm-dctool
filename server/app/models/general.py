from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base
from .academics import AuditMixin

class CountryGroup(Base, AuditMixin):
    __tablename__ = "country_group"

    country_group_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)

class Country(Base, AuditMixin):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    region = Column(String(255))
    continent = Column(String(255))
    country_dialing_code = Column(String(100))

class ProvinceOrState(Base, AuditMixin):
    __tablename__ = "province_or_state"

    province_or_state_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    country_id = Column(Integer, ForeignKey("country.country_id"))

    country = relationship("Country")

class City(Base, AuditMixin):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    province_or_state_id = Column(Integer, ForeignKey("province_or_state.province_or_state_id"))
    google_map_url = Column(String(500))
    latitude = Column(Float)
    longitude = Column(Float)

    province = relationship("ProvinceOrState")

class CountryCountryGroup(Base, AuditMixin):
    __tablename__ = "country_country_group"

    country_country_group_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    country_id = Column(Integer, ForeignKey("country.country_id"))
    country_group_id = Column(Integer, ForeignKey("country_group.country_group_id"))

class Location(Base, AuditMixin):
    __tablename__ = "location"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String(255))
    location_description = Column(Text)
    location_type = Column(String(100)) # Enum
    entity_id = Column(Integer)
    entity_type = Column(String(100))
    address_line_1 = Column(String(255))
    address_line_2 = Column(String(255))
    address_line_3 = Column(String(255))
    city_id = Column(Integer, ForeignKey("city.city_id"))
    province_or_state_id = Column(Integer, ForeignKey("province_or_state.province_or_state_id"))
    country_id = Column(Integer, ForeignKey("country.country_id"))
    postal_code = Column(String(50))
    location_urbanage = Column(String(100))
    latitude = Column(Float)
    longitude = Column(Float)
    google_map_url = Column(String(500))
    location_notes = Column(Text)

class ContactDetails(Base, AuditMixin):
    __tablename__ = "contact_details"

    contact_details_id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)
    isd_code = Column(String(10))
    phone_area_code = Column(String(10))
    phone_number1 = Column(String(50))
    phone_type1 = Column(String(50))
    phone_number2 = Column(String(50))
    phone_type2 = Column(String(50))
    contact_hours = Column(String(255))
    time_zone_id = Column(Integer)
    working_days = Column(String(255))
    email1 = Column(String(255))
    email_type1 = Column(String(100))
    email2 = Column(String(255))
    email_type2 = Column(String(100))
    email3 = Column(String(255))
    email_type3 = Column(String(100))
    email4 = Column(String(255))
    email_type4 = Column(String(100))
    url = Column(String(255))
    linked_in_address = Column(String(255))
    github_address = Column(String(255))
    facebook_page = Column(String(255))
    instagram_page = Column(String(255))
    contact_notes = Column(Text)
