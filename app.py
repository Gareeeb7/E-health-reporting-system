from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
import random
import time
import os
import json
import psycopg2
import requests as req

app = Flask(__name__)
api = Api(app)





def checkPostedData(postedData, functionName):
    if (functionName == "contact" or functionName == "digreport" or functionName == "viewlogs"):
        if "x" not in postedData or "y" not in postedData:
            return 301 #Missing parameter
        else:
            return 200
    elif (functionName == "home"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        else:
            return 200

class contact(Resource):
    def post(self):
        #If I am here, then the resouce contact was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "contact")
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: contact the posted data
        ret = x+y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class digreport(Resource):
    def post(self):
        #If I am here, then the resouce digreport was requested using the method POST

        #Step 1: Get posted data:
        while(True):
            postedData = request.get_json()

            #Steb 1b: Verify validity of posted data
            status_code = checkPostedData(postedData, "digreport")


            if (status_code!=200):
                retJson = {
                    "Message": "An error happened",
                    "Status Code":status_code
                }
                return jsonify(retJson)

            #If i am here, then status_code == 200
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            #Step 2: digreport of the posted data
            weight = x
            height = y

            retMap = {
                "Patient name": "Natahsa",
                'Gender': "Male",
                'Weight': weight,
                "Blood group": "O -ve",
                'Blood pressure (Systolic)': str(random.randint(70,90))+" mg%",
                'Blood pressure (Diastolic)': str(random.randint(115,125))+" mg%",
                'Body Temprature': 99.4,
                'Height': height,
                'Alergies': "NA",
                'Time': "time.localtime()",
                'Message': "Patient is curretly sleeping need care now, Code blue",
                'Sugar level': str(random.randint(100,180))+" mg/dL",
                'Status Code': 200,
                'Heamoglobin': "11.2 gm",
                'WBC Count': "2600 cm",
                'LYMPH%': str(random.randint(35,45))+" %",
                'EOSINO%': str(round(random.random(),2))+ " %",
                "PDW":  str(round(random.uniform(11,14),2))+" fl",
                "MPV": str(round(random.uniform(9,14),2))+" fl",
                "P-LCR": str(round(random.uniform(30,35),2))
            }

            time = time.localtime()
            bp_up = random.randint(70,90)
            bp_down = random.randint(115,125)
            temp = round(random.uniform(98,99),2)
            sugar = random.randint(100,180)
            wbc = random.randint(2600,3200)
            lymph= random.randint(35,45)
            eosino= round(random.random(),2)
            pdw = round(random.uniform(11,14),2)
            mpv = round(random.uniform(9,14),2)
            p_lcr = round(random.uniform(30,35),2)

            connection = psycopg2.connect(user="paeumtxy",password="5IklhXEIs4AqtLFLiCpaygieSpHEDcP1",host="john.db.elephantsql.com",port="5432",database="paeumtxy")
            cursor = connection.cursor()
            query = """ INSERT INTO lykanhos VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = ('Natasha', 'Female', 64, bp_up, bp_down, temp, time, sugar, 11, wbc, lymph, eosino, pdw, mpv, p_lcr)
            cursor.execute(query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into mobile table")

            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        return jsonify(retMap)


class viewlogs(Resource):
    def post(self):
        #If I am here, then the resouce viewlogs was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "viewlogs")


        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: viewlogs the posted data
        ret = x*y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class home(Resource):
    def post(self):
        #If I am here, then the resouce home was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "home")


        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: viewlogs the posted data
        ret = (x*1.0)/y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)



api.add_resource(contact, "/contact")
api.add_resource(digreport,"/digreport")
api.add_resource(viewlogs, "/viewlogs")
api.add_resource(home, "/home")

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/auth')
def auth():
    return render_template('login.html')


if __name__=="__main__":
    app.run(debug=True)
