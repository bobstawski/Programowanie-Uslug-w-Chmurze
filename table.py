from azure.cosmosdb.table.tableservice import TableService
# from azure.cosmosdb.table.models import Entity

account_name = 'bobstawski'
account_key = 'confidential'
table_service = TableService(account_name=account_name, account_key=account_key)


table_name = 'SampleTable1'
table_service.create_table(table_name)

#Crud
entity = {'PartitionKey': 'tasksPK', 'RowKey': '1', 'description': 'Task 1', 'priority': 1}
table_service.insert_entity(table_name, entity)

#cRud
task = table_service.get_entity(table_name, 'tasksPK', '1')
print("Dane pobrane z tabeli:")
print(task)

#crUd
task['priority'] = 2
table_service.update_entity(table_name, task)

#crUd
updated_task = table_service.get_entity(table_name, 'tasksPK', '1')
print("\nZaktualizowane dane:")
print(updated_task)

#cruD
table_service.delete_entity(table_name, 'tasksPK', '1')

table_service.delete_table(table_name)
