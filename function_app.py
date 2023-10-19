import azure.functions as func
import json
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
import logging
import os
import uuid

cosmos_endpoint = os.environ["COSMOS_ENDPOINT"]
cosmos_key = os.environ["COSMOS_KEY"]
cosmos_databaseId = os.environ["COSMOS_DATABASE"]
cosmos_containerId = os.environ["COSMOS_CONTAINER"]
eventHub_name = os.environ["EVENTHUB_NAME"]

# can be used instead of a key if you have configured Managed Identity for the Function App
#credential = DefaultAzureCredential()
#client = CosmosClient(url=endpoint, credential=credential)
client = CosmosClient(url=cosmos_endpoint, credential=cosmos_key)
database = client.get_database_client(cosmos_databaseId)
container = database.get_container_client(cosmos_containerId)

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", 
                               event_hub_name=eventHub_name,
                               connection="EVENTHUB_CONNECTION_STRING")                           

def eventhub_trigger(azeventhub: func.EventHubEvent):

    message = azeventhub.get_body().decode('utf-8')

    logging.info('Python EventHub trigger received an event: %s',
                message)

    message_json = json.loads(message)

    # add id property for Cosmos
    uid = str(uuid.uuid4())
    message_json['id'] = uid

    container.create_item(message_json)

    logging.info('Wrote message to Cosmos with Id: %s', uid)
    
