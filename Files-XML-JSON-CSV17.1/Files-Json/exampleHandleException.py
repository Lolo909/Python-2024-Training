import json
# ?????????????????? why not work?

# try:
# 	with open('data.json', 'r') as file:
#     	data = json.load(file)
# 	print(data)
# except json.JSONDecodeError as e:
# 	print(f"Error decoding JSON: {e}")
	

try:
	print(4)
except ValueError as e:
	print(e)
