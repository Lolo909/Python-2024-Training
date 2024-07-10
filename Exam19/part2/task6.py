# Task 6 - File Handling and Data Manipulation:
# Create a Python program that reads a CSV file named 'data.csv.' Each line in the CSV file contains a 
# student's name and their score separated by a comma (e.g., "Alice,85"). Write a function that reads this CSV file, 
# calculates the average score of all students, and saves the names of 
# students who scored above the average to a new text file named 'above_average.txt,' one name per line.
# 
# Example data:
# Alice,85
# Bob,92
# Charlie,78
# David,95
# Eve,88
# Frank,75
# Grace,98
# Hank,84
# Ivy,90
# Jack,70

import csv

def CSV_data_calculater(fileNameToRead):
	
    sumOfScores = 0;
    averageScore = 0;
    countStudents = 0;

    listWithSudentsWhichScoreIsAboveAverage = []


    with open('Exam19\part2\\' + str(fileNameToRead), 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            countStudents+=1
            sumOfScores += int(row[1])

        averageScore = sumOfScores / countStudents

    with open('Exam19\part2\\' + str(fileNameToRead), 'r', newline='') as file:
        reader = csv.reader(file)

        for  row in reader:
            if float(row[1]) > averageScore:
                listWithSudentsWhichScoreIsAboveAverage.append([row[0], row[1]])

    with open('Exam19\part2\\above_average.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in listWithSudentsWhichScoreIsAboveAverage:
            writer.writerow(row)

CSV_data_calculater("data.csv")