List Comprehension:
===================

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

numbers = [1, 2,3]
#new_lists = [new_item for item in lists]
new_lists = [n + 1 for n  in numbers]
print(new_lists)
[2, 3, 4]
    --------------------
  
Conditional List Comprehension:
============================


names = ["Suresh", "Ram", "Radha", "Banu", "Kumaran"]
new_lists = [new_item for item in lists if tests]
new_lists = [names.upper() for name in names if len(names) > 5]

results: 
=======

['SURESH', 'RADHA', 'KUMARAN']
-----------------------------



Traditional syntax:
================

new_list = []
for n in numbers:
  add_1 = n +1
  
  new_list.append(add_1)
--------------------

==================
Range_Comprehenstion:
==================

#new_lists = [new_item for item in lists]
new_list = [n * 2 for n in range (1,5)
print(new_list)

Results:
            
[2, 4, 6, 8]
            
            
=================
string Comprehention:
=================
#new_lists = [new_letter for letter in string]           
name = "Suresh"
            
letter_list = [new_letter for letter in string]
            
=================
            
Ang
====
 #For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)

=======================
            
Code Challenges:
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
3
Instructions:
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

Example:
  
file1.txt
=========                   
3
6
5
8
42
13

file2.txt
=========
3
6
34
1
344
42

main.py
======


with open ("file1.txt",) as file1 :
    file_1_data = file1.readlines()

with open ("file2.txt") as file2:
    file_2_data = file2.readlines()
   
 result = [new_item for item in list if test ]#in /not in 

result = [int(num) for num in file_1_data if num in file_2_data]

print(result)

Result:
[3,6,]
            
         
