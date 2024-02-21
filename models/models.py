from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from enum import Enum
from models.config import session, engine


Base = declarative_base()

class RoleEnum(Enum):
    COMMERCIAL = "commercial"
    SUPPORT = "support"
    GESTION = "gestion"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String(10), nullable=False)



meta_base = Base.metadata
meta_base.create_all(engine)



