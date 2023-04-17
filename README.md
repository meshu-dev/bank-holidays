# Bank Holidays

A small app built with Python / Flask to show the next UK Bank Holiday.

## Setup

-  Copy .env-example to .env and fill in variables

```
cp .env-example .env
```

-  Run command to import UK bank holidays data to SQLite

```
flask --app=app/main.py import-data
```

-  Run app

```
flask --app=app/main.py run
```

-  Run app with debug flag

```
flask --app=app/main.py --debug run
```

Go to url to view app which should be http://127.0.0.1:5000.

## Generate requirements.txt

Install the following to get packages for project.

```
pip install pipreqs
```

While inside project folder run pipreqs to generate requirements.txt file.

```
pipreqs .
```

## ToDo

App hasn't been setup on a server yet.

Will update instructions after site is live.
