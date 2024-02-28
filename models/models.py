from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from enum import Enum
from models.config import session, engine
import bcrypt
from datetime import datetime


Base = declarative_base()

class RoleEnum(Enum):
    COMMERCIAL = "commercial"
    SUPPORT = "support"
    GESTION = "gestion"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    role = Column(String(10), nullable=False)

    def __str__(self):
        return f'{self.id} - {self.username} / {self.role}'

    def __repr__(self):
        return f'{self.id} - {self.username} / {self.role}'
    
    def set_password(self, password): 
        # Hache le mot de passe avec bcrypt avant de le stocker
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        # Vérifie si le mot de passe correspond au hachage stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    company_name = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)
    last_contact = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    sales_contact_id = Column(Integer, ForeignKey("users.id"))
    sales_contact = relationship("User")

    def __str__(self):
        return f'{self.id} - {self.name} / {self.email}'

    def __repr__(self):
        return f'{self.id} - {self.name} / {self.email}'

class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship("Client")
    sales_contact_id = Column(Integer, ForeignKey("users.id"))
    sales_contact = relationship("User")
    total_amount = Column(Integer)
    remaining_amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    status = Column(Boolean, default= False)

    def __str__(self):
        return f'{self.id} - client : {self.client} / {self.total_amount} / {self.remaining_amount} / {self.status}'

    def __repr__(self):
        return f'{self.id} - client :{self.client} / {self.total_amount} / {self.remaining_amount} / {self.status}'

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    contract = relationship("Contract")
    support_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    support = relationship("User")
    event_date_start = Column(DateTime)
    event_date_end = Column(DateTime)
    location = Column(String(200))
    attendees = Column(Integer)
    notes = Column(String(500))


meta_base = Base.metadata



