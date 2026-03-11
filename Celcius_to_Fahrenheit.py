"""
Ques. Write a Python program to convert temperature in degree Celsius to degree Fahrenheit.
If water boils at 100 degree C and freezes as 0 degree C, 
use the program to find out what is the boiling point and
freezing point of water on the Fahrenheit scale.
(Hint: T(°F) = T(°C) × 9/5 + 32)
"""
#boiling point =100 degree C
#freezing point=0 degree C

Celcius_boiling_point = 100
Celcius_freezing_point = 0

Fahrenheit_boiling = (Celcius_boiling_point * 9/5) + 32
Fahrenheit_freezing = (Celcius_freezing_point * 9/5) + 32

print("Boiling point of water in Fahrenheit:", Fahrenheit_boiling, "F")
print("Freezing Point of water in Fahrenheit:", Fahrenheit_freezing,"F")