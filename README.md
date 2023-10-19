# Sample - Writing to CosmosDB NoSQL from a Python Azure Function
This reop contains a sample Azure Function that listens for messages on an EventHub and write those messages to CosmosDB for NoSQL.  The function requires the following app settings - these can either be set in local.settings.json (if running locally), or as Function configuration settings (if deployed to Azure).

| Setting | Description | Example |
| --- | --- | --- |
| EVENTHUB_CONNECTION_STRING  | A connection string for the Event Hub namespace | Endpoint=sb://\<name\>.servicebus.windows.net/;SharedAccessKeyName=\<name\>;SharedAccessKey=\<key\> |
| EVENTHUB_NAME | The name of the Event Hub to listen on | |
| COSMOS_ENDPOINT | The FQDN of your Cosmos DB NoSQL account  |  https://\<name\>.documents.azure.com:443/ |
| COSMOS_KEY | A read-write Cosmos DB key | |
| COSMOS_DATABASE | The name of the Cosmos database | |
| COSMOS_CONTAINER | The name of the Cosmos container | |


> **Important**
> We **strongly** recommend that you store key values in Azure Key Vault and use Kev Vault references in your App config settings. Details on how to configure App Service settings to use Key Vault are [here](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references?tabs=azure-cli#source-app-settings-from-key-vault). Note that you will also need to give yourself appropriate permissions to create secrets in the Key Vault.

> **Note**
> This repo uses the Azure Cosmos DB Python SDK to connect to and write messages to CosmosDB.  An alternative approach would be to use the Cosmos DB output binding (details [here](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-output?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cextensionv4&pivots=programming-language-python))


### Links

[Azure Functions Python Developer Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators)

[Event Hub Function Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2%2Cextensionv5&pivots=programming-language-python)

[Cosmos Python Quick Start](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python)


