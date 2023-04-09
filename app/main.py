from flask import Flask, render_template
from config import get_config
from holidays import import_holidays
from db.holidays import get_all_bank_holidays, get_next_bank_holiday, get_bank_holiday_by_name_and_date
from utils import get_day_suffix

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

@app.route('/')
def index():
    next_holiday = get_next_bank_holiday()
    day = next_holiday.date.day
    suffix = get_day_suffix(day)

    return render_template(
        'index.html',
        title='Next bank holiday',
        next_bank_holiday=next_holiday,
        suffix=suffix
    )

@app.cli.command('import-data')
def import_data():
    import_holidays()

if __name__ == '__main__':
    app.run(host="localhost", port=8000)
