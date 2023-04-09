from flask import Flask, render_template
import click
from config import get_config
from holidays import import_holidays
from db.holidays import get_all_bank_holidays, get_next_bank_holiday, get_bank_holiday_by_name_and_date

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

@app.route('/')
def index():
    next_holiday = get_next_bank_holiday()
    day = next_holiday.date.day

    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    return render_template(
        'index.html',
        title='Next bank holiday',
        next_bank_holiday=next_holiday,
        suffix=suffix
    )

@app.route('/test')
def test():
    holidays = get_all_bank_holidays()

    for holiday in holidays:
        print('DB Holiday', holiday.name, holiday.date)

    return render_template('index.html')

@app.cli.command('import-data')
def import_data():
    import_holidays()

print('name', __name__)

if __name__ == '__main__':
    app.run(host="localhost", port=8000)
