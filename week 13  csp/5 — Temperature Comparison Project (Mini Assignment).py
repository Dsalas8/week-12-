# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
Temp = int(input("Enter todays temperature: "))
# Prints whether it’s cold, warm, or hot using comparison operators.
if Temp < -10:
    print("Extreme Temperature Warning!!")
if 70 <= Temp <= 85:
    print("Its warm")
if -10 <= Temp < 70:
    print("Its cold")
if 85 <= Temp < 110:
    print("Its hot")
if 110 <= Temp:
    print("Extreme Temperature Warning!!")

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

