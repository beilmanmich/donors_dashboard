#Python 2.7.12
#Check Heroku Mlab for deployment version - pymongo 3.2.1 specified in requirements.txt

from flask import Flask
from flask import render_template
import pymongo
from pymongo import MongoClient
import json
import os
from urlparse import urlparse
from bson import json_util
from bson.json_util import dumps



app = Flask(__name__)

#Keep for local testing#
#MONGODB_HOST & MONDB_PORT Don't matter for heroku deploy - keep for local testing.
#MONGODB_HOST = 'localhost'
#MONGODB_PORT = 27017

#REPLACE WITH RESPECTIVE CREDENTIALS
MONGO_URI = 'mongodb://<user>:<pass>@ds11XXXX.mlab.com:1XXXX/donorschoose'
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/donorschoose/projects")
def donorschoose_projects():
    connection = MongoClient(MONGO_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    #You may be required to test row limits upon deploy, check Heroku logs for H12 error - timeout when calling jqueries. 
    #You can also combat this with gunicorn specifications found in Procfile -- "web: gunicorn school_donations:app --timeout 30 --keep-alive 5 --log-level debug"
    projects = collection.find( {} ,FIELDS).sort("_id", 1)#.limit(300000)
    #projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run() #debug=True #keep for local testing: host='0.0.0.0',port=5000,