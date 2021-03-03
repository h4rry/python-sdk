import os
from devo.api import Client, ClientConfig, SIMPLECOMPACT_TO_OBJ
import json

#key = os.getenv('DEVO_API_KEY', None)
#secret = os.getenv('DEVO_API_SECRET', None)
#url = os.getenv('DEVO_API_URL', None)

url="https://apiv2-us.devo.com/search"
auth=json.loads(open("creds.json","r").read())

api = Client(auth=auth,
             address="{}/query".format(url),
             config=ClientConfig(response="json/simple/compact",
                                 stream=True, processor=SIMPLECOMPACT_TO_OBJ))


query=open("query.txt").read()

response = api.query(query=query,
                     dates={'from': "today()-1*day()"})

for item in response:
    print(item)
