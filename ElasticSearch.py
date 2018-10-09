from elasticsearch import Elasticsearch
import json


# Define a default Elasticseach client
es = Elasticsearch(
    [
        'https://admin:XERLLJHHVHBLGUKE@portal-ssl1253-18.bmix-dal-yp-18454179-a761-42ac-8756-f4f03b0e1285.3057846300.composedb.com:58070/'])

MyFile = open("C:/SQL_Node/Achu/analysis.json", 'r').read()

ClearData = json.loads(MyFile)
i = 1

# Setting the index and type and ID for each tweet
# to upload the file to elastic search 
for line in ClearData:
    es.index(index='tweets_trump', doc_type='analysis', id=i, body=line)
    i = i + 1