from azure.cosmos import CosmosClient, PartitionKey

url = 'https://polska-lab1.documents.azure.com:443/'
key = 'confidential'
client = CosmosClient(url, credential=key)

database_name = 'ToDoDatabase'
container_name = 'ToDoList'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Crud
item = {
    "id": "10",
    "category": "personal",
    "name": "reminder",
    "description": "Whats up?",
    "isComplete": "False",
}
container.create_item(body=item)

#cRud
item_list = list(container.read_all_items(max_item_count=10))
print('Found {0} items'.format(item_list.__len__()))

response = container.read_item(partition_key="personal", item = "10")
print("Pobrany element:")
print(response)

#crUd
item['description'] = "Updated description"
updated_item = container.replace_item(item = "10", body = item)

response = container.read_item(partition_key="personal", item = "10")
print("Pobrany element:")
print(response)

#cruD
container.delete_item(partition_key="personal", item = "10")
