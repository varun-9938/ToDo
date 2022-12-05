from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL = "mysql://root:Varun0103@127.0.0.1:3306/todo"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()