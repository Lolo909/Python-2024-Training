ticketPrice = 0;

print("Insert your age:");
age = int(input())

if age < 12:
    ticketPrice = 5;
elif age < 18:
    ticketPrice = 7;
else:
    ticketPrice = 12;

print("Your ticket will cost",ticketPrice)