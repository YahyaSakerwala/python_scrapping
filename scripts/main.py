import json
from elasticsearch import Elasticsearch
from scrapeFunctionsmodule import ap_news,asahi_news


ELASTIC_PASSWORD = "u+57PJ9fhhtP4ayv_wE1"
api_key = 'djZSVGNvd0Jqc0JzMzBZTGxVamI6cVRsS1lsOXNSOG1DZjl5R2lPUldoZw=='
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="C:\\ElasticKibana\\kibana-8.11.3\\data\\ca_1702548513853.crt",
    # basic_auth=("elastic", ELASTIC_PASSWORD)
    api_key=api_key
)

print(client.ping())


# if __name__ == "__main__":
#     ap_news.scrape_ap_news()
#     asahi_news.scrape_asahi_news()


# with open("data/ap_news.json","r") as f:
#     json_objects = json.load(f)
#     f.close() 


# for json_doc in json_objects:
#     doc_id=json_doc['url']
#     response = client.index(index="ap_news", body=json_doc, id=doc_id)

# with open("data/asahi_news.json","r") as f:
#     json_objects = json.load(f)
#     f.close() 

# for json_doc in json_objects:
#     doc_id=json_doc['url']
#     response = client.index(index="asahi_news", body=json_doc, id=doc_id)