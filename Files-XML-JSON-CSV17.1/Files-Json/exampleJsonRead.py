import json

# Read JSON from a file
with open('Files-Json\\data.json', 'r') as file:
	data = json.load(file)

# Access data as a Python object
print(data)
