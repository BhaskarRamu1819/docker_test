from flask import Flask, jsonify, request
import pymongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)


# myclient = pymongo.MongoClient(host='host.docker.internal', port=27017) #docker
myclient = pymongo.MongoClient("mongodb://localhost:27017/") #local
mydb = myclient["employees_details"]
mycoll = mydb["Employees"]


def updated_result():
    new_list = []
    for e in mycoll.find():
        # e["_id"] = str(e["_id"])
        new_list.append({
            "id": e["id"],
            "name": e["name"],
            "role": e["role"],
            "state": e["state"]
            })
    return new_list
result = updated_result()
# print(result)
@app.route("/")
def initial():
    return 'Flask Project with CRUD operations'

#with GET method to read the employes details at get function
@app.route("/employees", methods=["GET"])
def get():
    return jsonify({"employes": result})

#get unique employe details with query of id
@app.route("/employees/<state>", methods=["GET"])
def get_id(state):
    try:
        specific = []
        data = mycoll.find({"state":state})
        for items in data:
            items.pop("_id")
            for key in list(items):
                items[key] = str(items[key])
            specific.append(items)
        string = "Employee Details are Not Avalable"
        results = specific if specific != [] else string
        return jsonify({"employee": results})
    except Exception as ex:
        return str(ex)


