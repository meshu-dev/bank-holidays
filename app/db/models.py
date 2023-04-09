from sqlalchemy import create_engine, inspect, MetaData, Table
from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy import select, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from db.database import db_init

Base = declarative_base()

engine = db_init()
session = Session(engine)

class BankHoliday(Base):
    __tablename__ = "bank_holidays"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)

Base.metadata.create_all(engine)

