# Task 6: You are provided with a list of dictionaries, where each dictionary represents a student's information. 
# Each dictionary contains the following keys: "name," "scores," and "subject." The "scores" key maps to a list of 
# exam scores for a particular subject. Your task is to perform the following:

# Calculate the average score for each student.
# Find the student with the highest average score.
# Create a set of subjects that all students have taken.
# Here's a sample list of student data:
# students = [
#     {
#         "name": "Alice",
#         "scores": [85, 90, 78],
#         "subject": "Math",
#     },
#     {
#         "name": "Bob",
#         "scores": [92, 88, 95],
#         "subject": "Math",
#     },
#     {
#         "name": "Charlie",
#         "scores": [78, 80, 85],
#         "subject": "Science",
#     },
#     # Add more student data as needed
# ]

# Write Python code to perform these tasks and print the results.

students = [
    {
        "name": "Alice",
        "scores": [85, 90, 78],
        "subject": "Math",
    },
    {
        "name": "Bob",
        "scores": [92, 88, 95],
        "subject": "Math",
    },
    {
        "name": "Charlie",
        "scores": [78, 80, 85],
        "subject": "Science",
    },
    # Add more student data as needed
]


highestAverageScore = 0
studentNameWithTheHighestScore = ""

allSubjectThatAllStudentsHaveTaken = set()

for student in students:
    average = 0;
    listWithScores = student["scores"]

    for score in listWithScores:
        average += score
    
    average = average / len(listWithScores)

    allSubjectThatAllStudentsHaveTaken.add(student["subject"])

    if highestAverageScore < average:
        highestAverageScore = average
        studentNameWithTheHighestScore = student["name"]

    print(student["name"] + " has " + "{:.2f}".format(average) + " average score in " + student["subject"])

print("---------------")
print(studentNameWithTheHighestScore + " is the student with the highest average score of " + "{:.2f}".format(highestAverageScore))

print("---------------")
print("All subject that have been taken by the sudents:")
print(allSubjectThatAllStudentsHaveTaken)