import os
import sys
import json
import pymongo
import config

DB_NAME = 'api'
# setup pymongo backend
client = pymongo.MongoClient(config.MONGODB_URL)
client.drop_database(DB_NAME)

# clear API DB if known.
db = client.api
# The top argument for walk
topdir = sys.argv[1]
# The extension to search for
exten = '.json'
data = []
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            if 'site' not in dirpath and 'github' not in dirpath:
                data.append(os.path.join(dirpath, name))

for json_file in data:
    print(json_file)
    with open(json_file) as json_file:
        json_data = json.load(json_file)
        db.findings.insert_one(json_data)

# build index
db.findings.create_index(
    [('finding.findingDetails.findingMatrix.id',    pymongo.ASCENDING)], unique=True)
db.findings.create_index(
    [('finding.findingDetails.findingMatrix.title', pymongo.ASCENDING)], unique=False)
db.findings.create_index(
    [('finding.findingDetails.findingMatrix.vsr',   pymongo.ASCENDING)], unique=False)
db.findings.create_index(
    [('finding.findingDetails.findingMatrix.cvss',  pymongo.ASCENDING)], unique=False)
db.findings.create_index(
    [('finding.findingDetails.findingMatrix.risk',  pymongo.ASCENDING)], unique=False)
