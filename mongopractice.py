
from pymongo import MongoClient
import re

client = MongoClient('mongodb://mbdsuser:mbds2017@34.211.148.131:27017/mbdsdb')

mydb = client['mbdsdb']

myCollection = mydb['bigdatasurvey']

#entry = {"name": "Joey Bingham", "nondb": {"excel": True, "flatfile": True}, "db":{"sql": False, "nosql":{"document": False, "graph": False}}, "size":{"kb": True, "mb": True, "gb": True, "tb":True}}

#myCollection.insert_one(entry)

#regex use re package

#pattern = re.compile("[Eric.*]$")

#query = {"name": pattern}

#query = {"size.tb": False}


objs = myCollection.find(query)

count = 0
for item in objs:
#    print item
     count += 1
print count

