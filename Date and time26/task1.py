# Task 1: Age Calculator:
# Create a function that takes a birthdate as input and calculates the person's age in years.

birthday = input("Insert your birthday like this(day month year):")
day=int(birthday.split()[0])
month = int(birthday.split()[1])
year = int(birthday.split()[2])

from datetime import datetime

current_datetime = datetime.now()
yearNow = current_datetime.year

print(f"You are {yearNow-year} years wise :)")