# Tuple Concatenation and Repetition: Create two tuples, one containing the days of the week (Monday through Sunday) 
# and another containing the corresponding temperatures (in degrees Celsius). Perform the following operations:
# Combine the two tuples to create a list of tuples with the day of the week and the temperature for this day.
# Repeat the week's weather forecast three times.
# Print the information about the forecast

daysOfTheWeek = ("Monday", "Thusday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
degreesInCelsius = (28,32,33,30,33,29,35)

weekForecast = list(zip(daysOfTheWeek,degreesInCelsius))
threeWeekForecast = weekForecast*3

print(threeWeekForecast)
