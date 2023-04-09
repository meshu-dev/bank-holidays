from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from db.database import db_init
from db.models import BankHoliday

Base = declarative_base()

engine = db_init()
session = Session(engine)

def add_bank_holiday(params):
    bank_holiday = BankHoliday(
        name=params['name'],
        date=params['date']
    )
    session.add(bank_holiday)
    session.commit()

    return bank_holiday

def get_bank_holiday(id):
    bank_holiday = session.query(BankHoliday).filter_by(id=id).first()
    return bank_holiday

def get_bank_holiday_by_name_and_date(name, date):
    bank_holiday = session.query(BankHoliday).filter_by(name=name, date=date).first()
    return bank_holiday

def get_all_bank_holidays():
    bank_holidays = session.query(BankHoliday).all()
    return bank_holidays

def edit_bank_holiday(id, params):
    bank_holiday = session.query(BankHoliday).filter_by(id=id).first()
    bank_holiday.name = params['name']
    bank_holiday.date = params['date']
    
    session.add(bank_holiday)
    session.commit()

    return crypto

def delete_bank_holiday(id):
    bank_holiday = session.query(BankHoliday).filter_by(id=id).first()

    session.delete(bank_holiday)
    session.commit()
