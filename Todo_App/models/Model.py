import json
from database.Db_Conn import Base
from sqlalchemy import Column,Integer,String


class Task(Base):
    __tablename__='todos'
    id=Column(Integer,primary_key=True,index=True)
    # title=Column(String)
    body=Column(String)