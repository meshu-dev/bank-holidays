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
