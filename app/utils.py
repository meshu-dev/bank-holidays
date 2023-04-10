from os import path
from urllib.request import Request, urlopen

def get_content_from_url(url):
    req = Request(
        url=url
    )
    webUrl  = urlopen(url)
    data = webUrl.read()

    return data

def get_file_path(file):
    basedir = path.abspath(path.dirname(__file__))
    return path.join(basedir, file)

def get_day_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = 'th'
    else:
        suffix = ['st', 'nd', 'rd'][day % 10 - 1]
    
    return suffix
