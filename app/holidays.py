import json, time, datetime
from datetime import date
from time import gmtime, strftime
from utils import get_content_from_url
from config import get_config
from db.holidays import add_bank_holiday

def get_bank_holiday_json():
    dataUrl = get_config('BANK_HOLIDAYS_URL')
    data = get_content_from_url(dataUrl)
    
    return data

def get_bank_holidays(division, json_data):
    uk_bank_holidays = json.loads(json_data)
    england_bank_holidays = uk_bank_holidays[division]
    days = england_bank_holidays['events']

    return days

def get_next_bank_holidays(division, json_data):
    days = get_bank_holidays(division, json_data)
    next_days = []

    for data in days:
        date = data['date']

        current_time = gmtime()
        holiday_date = time.strptime(date, '%Y-%m-%d')

        if holiday_date > current_time:
            next_days.append(data)

    return next_days

def add_holidays(days):
    for data in days:
        holiday = add_holiday(data['title'], data['date'])

        print('DB Holiday', holiday.name, holiday.date)

def get_holiday_date(date_str):
    date_data = date_str.split('-')

    year = int(date_data[0])
    month = int(date_data[1])
    day = int(date_data[2])

    holiday_date = date(year, month, day)
    return holiday_date

def add_holiday(name, date):
    holiday_date = get_holiday_date(date)

    params = {
        "name": name,
        "date": holiday_date
    }

    holiday = add_bank_holiday(params)
    return holiday

def import_holidays():
    bank_holidays_json = get_bank_holiday_json()
    days = get_next_bank_holidays('england-and-wales', bank_holidays_json)
    add_holidays(days)
