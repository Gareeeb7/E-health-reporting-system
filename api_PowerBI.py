import pandas as pd
from datetime import timedelta
import requests
import json
import urllib3
import psycopg2
import random
import time as t
from datetime import datetime

##class for data_generation


def data_generation():
    
    name = "Natasha"
    gender = "Female"
    age = 64
    time = datetime.now()
    blood_pressure_systolic = random.randint(70,90)
    blood_pressure_diastolic = random.randint(115,125)
    body_temperature = round(random.uniform(98,99),2)
    heamoglobin = 11
    sugar_level = random.randint(100,180)
    wbc_count = random.randint(2600,3200)
    lymph= round(random.uniform(35,45),2)
    eosino= round(random.random(),2)
    pdw = round(random.uniform(11,14),2)
    mpv = round(random.uniform(9,14),2)
    p_lcr = round(random.uniform(30,35),2)
    
    return [name, gender, age, blood_pressure_systolic, blood_pressure_diastolic, body_temperature, time, sugar_level, heamoglobin, wbc_count, lymph, eosino, pdw, mpv, p_lcr]


if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/179db03d-0981-4f91-9cdb-66db9925279e/datasets/6e838cab-f884-4973-8545-8604572ab374/rows?redirectedFromSignup=1&key=oga98QNM4b9WQLqWa3s4DKDIWi0q7a6gVSGJACCeAq%2FFE2cIevZAlk1YfYBmW0el328p%2FdzfbS4svFme7RrNNA%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["name", "gender", "age", "blood_pressure_systolic", "blood_pressure_diastolic", "body_temperature", "time", "sugar_level", "heamoglobin", "wbc_count", "lymph", "eosino", "pdw", "mpv", "p_lcr"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        t.sleep(2)

