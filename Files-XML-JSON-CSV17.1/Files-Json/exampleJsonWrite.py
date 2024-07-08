import json

# Python object
data = {
	"name": "John Doe",
	"age": 30,
	"city": "Exampleville",
	"interests": ["reading", "coding", "traveling"]
}

# Write Python object to a JSON file
with open('Files-Json\\output.json', 'w') as file:
	json.dump(data, file, indent=2)

