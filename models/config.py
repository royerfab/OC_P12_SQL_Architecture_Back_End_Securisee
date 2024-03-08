from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_NAME = "db_P12"
DB_USERNAME = "username"
DB_PASSWORD = "password"
DB_HOST = "localhost"
engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}', echo=False)
# engine = create_engine('sqlite:///database.db', echo = False)
conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
