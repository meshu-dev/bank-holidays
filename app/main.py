from flask import Flask, render_template
from config import get_config
from holiday.view import get_next_bank_holiday_data
from holiday.script import import_holidays

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

@app.route('/')
def index():
    next_holiday = get_next_bank_holiday_data()

    return render_template(
        'index.html',
        title='Next bank holiday',
        next_holiday_name=next_holiday['name'],
        next_holiday_date=next_holiday['date']
    )

@app.cli.command('import-data')
def import_data():
    import_holidays()

if __name__ == '__main__':
    app.run(host="localhost", port=8000)
