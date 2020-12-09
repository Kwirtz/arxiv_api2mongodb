# arxiv_api2mongodb
The goal of this repo is to dl the metadatas of arXiv articles.
For this there's 2 script:

- oai.py which uses the oai protocol to get the ids of the arXiv articles you want (currently Downloading every id)
- api.py which uses the ID of oai to download the metadatas and put it in a MongoDB

Feel free to change the oai query and the way to store data.
