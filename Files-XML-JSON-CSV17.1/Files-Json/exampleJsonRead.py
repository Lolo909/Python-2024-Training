import json

# Read JSON from a file Files-XML-JSON-CSV17.1\Files-Json
with open('Files-XML-JSON-CSV17.1\\Files-Json\\data.json', 'r') as file:
	data = json.load(file)

# Access data as a Python object
print(data)
