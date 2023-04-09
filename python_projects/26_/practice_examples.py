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


