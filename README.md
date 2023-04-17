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

## To do

App hasn't been setup on a server yet.

Will update instructions after site is live.
