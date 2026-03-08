import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
load_dotenv(dotenv_path=".env")

DATABASE_URL = os.getenv("DATABASE_URL")
assert DATABASE_URL is not None

# DBURL
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
