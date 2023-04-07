List Comprehension:
===================

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

numbers = [1, 2,3]

new_lists = [n + 1 for n  in numbers]
print(new_lists)
[2, 3, 4]

Traditional syntax:
================

new_list = []
for n in numbers:
  add_1 = n +1
  
  new_list.append(add_1)
--------------------
