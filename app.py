from flask import Flask
from flask import render_template
from pymongo import MongoClient
import pymongo
import json
from bson import json_util
from bson.json_util import dumps
from urlparse import urlsplit #
import os #

app = Flask(__name__)

uri = 'mongodb://ltest:test@ds115671.mlab.com:15671/herokup_rqr408rd'

client = MongoClient(uri)
db = client.get_default_database()

MONGODB_HOST = 'localhost'
MONGODB_PORT = 15671
DBS_NAME = 'donorschoosedashboard'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorschoosedashboard/projects")
def donorschoose_projects():
    connection = MongoClient(uri)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find( {} ,FIELDS)
    #projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)