from elasticsearch import Elasticsearch

# Define a default Elasticseach client
es = Elasticsearch(
    [
        'https://admin:XERLLJHHVHBLGUKE@portal-ssl1253-18.bmix-dal-yp-18454179-a761-42ac-8756-f4f03b0e1285.3057846300.composedb.com:58070/'])

# Query to fetch only Tweets with POSITIVE sentiment
response = es.search(
    index="tweets_trump", 
    body = {
        "query": {
            "match": {"Sentiment":"Neutral"}
        }

})

for hits in response['hits']['hits']:
    print(hits['_source'])

print("Total tweets::"+ str(response['hits']['total']))