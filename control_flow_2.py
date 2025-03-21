"""Write a Python program that asks the user for a number and prints "Even" if the number is even.

Ask the user for their age. If they are 18 or older, print "You can vote".

Write a Python program that asks the user for their exam score.
⦁	If the score is 50 or more, print "You passed!"
⦁	Otherwise, print "You failed!"

Write a program that asks the user for a number and checks if it is positive or negative.
⦁	If the number is greater than 0, print "Positive"
⦁	Otherwise, print "Negative"

Write a Python program that asks for the temperature and prints the weather condition.
⦁	If the temperature is above 35, print "Very Hot"
⦁	If the temperature is between 26 and 35, print "Warm"
⦁	If the temperature is between 15 and 25, print "Cool"

Write a program that asks for a car's speed.
⦁	If the speed is above 100 km/h, print "Overspeeding! Slow down."
⦁	If the speed is between 60 and 100 km/h, print "You are driving at a safe speed."
⦁	If the speed is below 60 km/h, print "You are driving too slow."


Ask the user for their exam score and print their grade:
⦁	80 and above → "Grade: A"
⦁	60 to 79 → "Grade: B"
⦁	40 to 59 → "Grade: C"
⦁	Below 40 → "Grade: F"

Write a program that asks for a year and checks if it is a leap year.
⦁	A year is a leap year if it is divisible by 4 but not divisible by 100, unless also divisible by 400.
⦁	Print "Leap Year" if true, otherwise print "Not a Leap Year"."""


# Write a Python program that asks the user for a number and prints "Even" if the number is even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")

#    Ask the user for their age. If they are 18 or older, print "You can vote".

age = int(input("Enter your age: ")) 
if age >= 18:
    print("You can vote")

'''Write a Python program that asks the user for their exam score.
⦁	If the score is 50 or more, print "You passed!"
⦁	Otherwise, print "You failed!"'''

score = int(input("Enter your score: "))
if score >= 50:
    print("You've passed!")
else:
    print("You've failed!")

'''Write a program that asks the user for a number and checks if it is positive or negative.
⦁	If the number is greater than 0, print "Positive"
⦁	Otherwise, print "Negative"'''

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Negative")

'''Write a Python program that asks for the temperature and prints the weather condition.
⦁	If the temperature is above 35, print "Very Hot"
⦁	If the temperature is between 26 and 35, print "Warm"
⦁	If the temperature is between 15 and 25, print "Cool"'''

temp = int(input("Enter the temperature: "))
if temp > 35:
    print("Very hot")
elif temp >= 26 and temp <= 35:
    print("Warm")
elif temp >= 15 and temp <= 25:
    print("Cool")



'''Write a program that asks for a car's speed.
⦁	If the speed is above 100 km/h, print "Overspeeding! Slow down."
⦁	If the speed is between 60 and 100 km/h, print "You are driving at a safe speed."
⦁	If the speed is below 60 km/h, print "You are driving too slow."'''

car_speed = int(input("Enter a car speed in km/h: "))
if car_speed > 100:
    print("Overspeeding! Slow down.") 
elif car_speed >= 60 and car_speed <= 100:
    print("You are driving at a safe speed.")
elif car_speed <= 60:
    print("You are driving too slow.")


'''Ask the user for their exam score and print their grade:
⦁	80 and above → "Grade: A"
⦁	60 to 79 → "Grade: B"
⦁	40 to 59 → "Grade: C"
⦁	Below 40 → "Grade: F"'''

exam_score = int(input("Enter your exam score: "))
if exam_score >= 80:
    print("Grade: A")
elif exam_score >= 60 and exam_score <= 79:
    print("Grade: B")
elif exam_score >= 40 and exam_score <= 59:
    print("Grade: C")
else: 
    print("Grade: F")


'''Write a program that asks for a year and checks if it is a leap year.
⦁	A year is a leap year if it is divisible by 4 but not divisible by 100, unless also divisible by 400.
⦁	Print "Leap Year" if true, otherwise print "Not a Leap Year"'''

year = int(input("Enter an year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

