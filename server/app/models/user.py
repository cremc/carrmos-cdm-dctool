from sqlalchemy import Boolean, Column, Integer, String
from ..database import Base
from .academics import AuditMixin

class User(Base, AuditMixin):
    __tablename__ = "user"

    users_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    db_role = Column(Integer, default=1) # 1:data_viewer, 2:data_entry_operator, 3:data_qcer, 4: data_collector1 and so on...
