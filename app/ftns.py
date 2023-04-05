import json
from dotenv import load_dotenv
from os import environ
from urllib.request import Request, urlopen

load_dotenv('.env')

def getContentFromUrl(url):
    req = Request(
        url=url
    )
    webUrl  = urlopen(url)
    data = webUrl.read()

    return data

def getBankHolidayJson():
    dataUrl = environ.get('BANK_HOLIDAYS_URL')
    data = getContentFromUrl(dataUrl)
    
    return data

def getBankHolidays(division, jsonData):
    ukBankHolidays = json.loads(jsonData)
    englandBankHolidays = ukBankHolidays[division]
    days = englandBankHolidays['events']

    return days

def addHolidays(days):
    for data in days:
        name = data['title']
        date = data['date']

        print('DAY', name, date)
        #print(key, '->', bankHolidayDict[key])

    #print(bankHolidayDict)
