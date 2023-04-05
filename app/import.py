from ftns import getBankHolidayJson, getBankHolidays, addHolidays

bankHolidaysJson = getBankHolidayJson()
days = getBankHolidays('england-and-wales', bankHolidaysJson)
addHolidays(days)
