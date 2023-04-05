import json
from dotenv import load_dotenv
from os import environ
from urllib.request import Request, urlopen

load_dotenv('.env')

def getBankHolidayJson():
    dataUrl = environ.get('BANK_HOLIDAYS_URL')
    data = getContentFromUrl(dataUrl)
    
    return data

def getContentFromUrl(url):
    req = Request(
        url=url
    )

    webUrl  = urlopen(url)
    data = webUrl.read()

    return data

def getBankHolidays(jsonData):
    bankHolidayDict = json.loads(jsonData)
    print(bankHolidayDict)
