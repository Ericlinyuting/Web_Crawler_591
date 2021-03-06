import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import datetime
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import io
import json
warnings.filterwarnings("ignore")

headers={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }

request_url='http://newhouse.591.com.tw/home/housing/info?hid=119282'
res=requests.get(request_url, headers = headers)
bs=BeautifulSoup(res.text,'html.parser')
