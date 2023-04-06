import json
from dotenv import load_dotenv
from os import environ
from urllib.request import Request, urlopen

load_dotenv('.env')

def get_content_from_url(url):
    req = Request(
        url=url
    )
    webUrl  = urlopen(url)
    data = webUrl.read()

    return data

def get_bank_holiday_json():
    dataUrl = environ.get('BANK_HOLIDAYS_URL')
    data = get_content_from_url(dataUrl)
    
    return data

def get_bank_holidays(division, json_data):
    uk_bank_holidays = json.loads(json_data)
    england_bank_holidays = uk_bank_holidays[division]
    days = england_bank_holidays['events']

    return days

def add_holidays(days):
    for data in days:
        name = data['title']
        date = data['date']

        print('DAY', name, date)
        #print(key, '->', bankHolidayDict[key])

    #print(bankHolidayDict)
