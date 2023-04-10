Examples:

1.
Instructions:
=============

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
You are going to write a List Comprehension to create a new list called squared_numbers. 
This new list should contain every number in the list numbers but each number should be squared.  

  Results:
  ========
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]

print(squared_numbers)
--------------------

2.
Instructions:
============
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
You are going to write a List Comprehension to create a new list called result. 
This new list should only contain the even numbers from the list numbers.

Results:
=======

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [n for n in numbers if n % 2 == 0 ]
print(result)

----------------

3.
You are going to use Dictionary Comprehension to create a dictionary called result that 
takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

  
result = {words: len(words) for words in sentence.split()}
print(result)

Results:
=======
{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

4.
Instructions
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes
each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f:

(temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {days : temp * 9/5 + 32 for (days, temp)  in weather_c.items() }

print(weather_f)

Results:
 =====

{'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
