from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('mysql+pymysql://username:password@localhost/db_P12', echo = False)
#engine = create_engine('sqlite:///database.db', echo = False)
conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
