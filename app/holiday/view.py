from db.holidays import get_next_bank_holiday
from utils import get_day_suffix

def get_next_bank_holiday_data():
    next_holiday = get_next_bank_holiday()

    day = next_holiday.date.day
    suffix = get_day_suffix(day)

    next_holiday_name = next_holiday.name
    next_holiday_date = next_holiday.date.strftime('%A {day}{suffix} %B %Y')
    next_holiday_date = next_holiday_date.replace('{day}', str(day))
    next_holiday_date = next_holiday_date.replace('{suffix}', suffix)

    data = {
        "name": next_holiday_name,
        "date": next_holiday_date
    }

    return data
