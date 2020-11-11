import json
import urllib3
import psycopg2
import random
import time as t
from datetime import datetime

connection = psycopg2.connect(user="paeumtxy",password="5IklhXEIs4AqtLFLiCpaygieSpHEDcP1",host="john.db.elephantsql.com",port="5432",database="paeumtxy")
cursor = connection.cursor()

while(True):
    time = datetime.now()
    bp_up = random.randint(70,90)
    bp_down = random.randint(115,125)
    temp = round(random.uniform(98,99),2)
    sugar = random.randint(100,180)
    wbc = random.randint(2600,3200)
    lymph= round(random.uniform(35,45),2)
    eosino= round(random.random(),2)
    pdw = round(random.uniform(11,14),2)
    mpv = round(random.uniform(9,14),2)
    p_lcr = round(random.uniform(30,35),2)
    t.sleep(1)

    query = """ INSERT INTO lykanhos VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = ('Natasha', 'Female', 64, bp_up, bp_down, temp, time, sugar, 11, wbc, lymph, eosino, pdw, mpv, p_lcr)
    cursor.execute(query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into mobile table")

