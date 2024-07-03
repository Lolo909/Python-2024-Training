print("Insert year:", end="")
year = int(input())

if year % 400 == 0:
    print("Year is leap.")
elif year % 4 == 0 and year % 100 != 0:
    print("Year is leap.")
else:
    print("Year is not leap")
