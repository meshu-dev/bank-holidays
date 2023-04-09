from flask import Flask, render_template
import click
from config import get_config
from holidays import import_holidays
from db.holidays import get_all_bank_holidays

app = Flask(__name__, template_folder='../templates')
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    holidays = get_all_bank_holidays()

    for holiday in holidays:
        print('DB Holiday', holiday.name, holiday.date)

    return render_template('index.html')

@app.cli.command('import-data')
def import_data():
    import_holidays()

print('name', get_config('TEST'))

if __name__ == '__main__':
    app.run(host="localhost", port=8000)
