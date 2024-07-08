import csv

# Read CSV from a file
with open('Files-CSV\\data.csv', 'r', newline='') as file:
	reader = csv.reader(file)
    
	# Access data row by row
	for row in reader:
    	 print(row)