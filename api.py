import requests
import feedparser
import tqdm
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client["arxiv"] 
collection = mydb["api"]


with open("./arxiv_ids_cs.txt","r") as lines:
    ids = lines.read().split("\n")[0:-2]

results = {}
ids_query = []
iteration = 1

for id_ in tqdm.tqdm(ids):
    if iteration % 100 != 0:
        iteration += 1
        ids_query.append(id_)
    else:
        ids_query = ",".join(ids_query)
        response = requests.get('http://export.arxiv.org/api/query?id_list={}&max_results=100'.format(ids_query))
        feed = feedparser.parse(response.content)
        list_of_insertion = []
        for entry in feed.entries:
            list_of_insertion.append(dict(entry))
        collection.insert_many(list_of_insertion)
        ids_query = []
        iteration = 1
        time.sleep(1/3)
    