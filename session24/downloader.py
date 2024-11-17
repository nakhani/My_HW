from threading import Thread
from time import time
import requests


def download(url):

    result = requests.get(url)
