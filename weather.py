#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from datetime import datetime

def soup_maker(link):
    result = requests.get(link)
    src = result.content
    soup_to_return = BeautifulSoup(src, 'lxml')
    return soup_to_return

def current_temp(soup_temp):
    temp_elems = soup_temp.select("#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--1_6ni > div._-_-components-src-organism-CurrentConditions-CurrentConditions--primary--2DOqs > span")
    return temp_elems[0].getText()

def conditions(soup_conditions):
    condi_elems = soup_conditions.select("#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--1_6ni > div._-_-components-src-organism-CurrentConditions-CurrentConditions--primary--2DOqs > div")
    return condi_elems[0].getText()

def rain_chance():
    soup_rain = soup_maker("https://weather.com/weather/hourbyhour/l/a6533731c9dcc4a2f52136195be34dc3d2a6bdb5a94ec69bd628c0185cd5db39")
    chance_elems = soup_rain.select("#WxuHourlyCard-main-74f43669-10ed-4577-a8c4-85ad9d041036 > section > div._-_-components-src-organism-HourlyForecast-HourlyForecast--DisclosureList--MQWP6 > details:nth-child(2) > summary > div > div > div._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O > span")
    return chance_elems[0].getText()

def high_temp(soup_high):
    high_elems = soup_high.select("#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--1_6ni > div._-_-components-src-organism-CurrentConditions-CurrentConditions--secondary--32-kp > div > span:nth-child(1)")
    return high_elems[0].getText()

def low_temp(soup_low):
    low_elems = soup_low.select("#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--1_6ni > div._-_-components-src-organism-CurrentConditions-CurrentConditions--secondary--32-kp > div > span:nth-child(2)")
    return low_elems[0].getText()

def feels_temp(soup_feels):
    feels_elems = soup_feels.select("#WxuTodayDetails-main-fd88de85-7aa1-455f-832a-eacb037c140a > section > div._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--hero--2QGgO > div._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTemp--2x1SW > span._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt")
    return feels_elems[0].getText()

def time_maker():
    today = datetime.now()
    formatToday = today.strftime("%B %d, %Y at %I:%M %p")
    return formatToday

soup = soup_maker("https://weather.com/weather/today/l/a6533731c9dcc4a2f52136195be34dc3d2a6bdb5a94ec69bd628c0185cd5db39")

#INFO
temp = current_temp(soup)
condition = conditions(soup)
precip = rain_chance()
high = high_temp(soup)
low = low_temp(soup)
feels = feels_temp(soup)
time = time_maker()

accountSID = 'REPLACE WITH TWILIOSID'
authToken = 'REPLACE WITH TWILIO TOKEN'
myNumber = 'REPLACE WITH YOUR NUMBER'
twilioNumber = 'REPLACE WITH TWILIO NUMBER'
numbers = [myNumber]

def text(message_1, recipient):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body = message_1, from_ = twilioNumber, to = recipient)

for number in numbers:
    text(message, number)
