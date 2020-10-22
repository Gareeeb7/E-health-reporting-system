from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if (functionName == "add" or functionName == "digreport" or functionName == "viewlogs"):
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

class Add(Resource):
    def post(self):
        #If I am here, then the resouce Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "add")
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

        #Step 2: Add the posted data
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

class Divide(Resource):
    def post(self):
        #If I am here, then the resouce Divide was requested using the method POST

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



api.add_resource(Add, "/add")
api.add_resource(digreport, "/digreport")
api.add_resource(viewlogs, "/viewlogs")
api.add_resource(Divide, "/home")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(debug=True)
