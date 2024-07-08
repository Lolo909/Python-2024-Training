import csv

# Python data
data = [
	["Name", "Age", "City"],
	["John Doe", 30, "Exampleville"],
	["Jane Smith", 25, "Sampletown"]
]

# Write Python data to a CSV file
with open('Files-CSV\\output.csv', 'w', newline='') as file:
	writer = csv.writer(file)
    
	# Write data row by row
	for row in data:
         writer.writerow(row)