from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
import tqdm

URL = 'http://export.arxiv.org/oai2?verb=ListIdentifiers&set=cs,econ&from=2006-01-01&until=2020-12-01'
registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)
client = Client(URL, registry)

arxiv_txt = open('./arxiv_ids_cs.txt', 'a')

for record in tqdm.tqdm(client.listRecords(metadataPrefix='oai_dc')):
    try:
        id_ = record[1].getMap()["identifier"][0].split("/")[-1]
        arxiv_txt.write(id_ + "\n")
    except:
        pass
arxiv_txt.close()
