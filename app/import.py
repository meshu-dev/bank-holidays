from utils import get_bank_holiday_json, get_bank_holidays, add_holidays

bank_holidays_json = get_bank_holiday_json()
days = get_bank_holidays('england-and-wales', bank_holidays_json)
add_holidays(days)
