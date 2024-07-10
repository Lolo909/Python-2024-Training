# Task 2: Event Countdown:
# Write a program that takes a future date as input and calculates the number of
# days, hours, and minutes remaining until that date.

from datetime import datetime

current_datetime = datetime.now()

isItRigthDate = False

while not isItRigthDate:
    futureDate = input("Insert future date like this(day month year):")
    day=int(futureDate.split()[0])
    month = int(futureDate.split()[1])
    year = int(futureDate.split()[2])

    date_string = f"{year}-{month}-{day}"
    parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d")

    if current_datetime < parsed_datetime:
        isItRigthDate = True
    else:
        print("Wrong date! Date must be in the FUTURE!!!")
    
print("Days:",(parsed_datetime - current_datetime).days)
print("Hours:",(parsed_datetime - current_datetime).days * 24)
print("Minutes:",(parsed_datetime - current_datetime).days * 24 * 60)