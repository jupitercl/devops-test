from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_USER = os.getenv('DB_USER', "devops")
DB_PASSWORD = os.getenv('DB_PASS', "devops")
DB_NAME = os.getenv('DB_NAME', "devops")
DB_HOST = os.getenv('DB_HOST', "db")
DB_PORT = os.getenv('DB_PORT', 5432)

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
