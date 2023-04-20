Exceptions:
==========
Errors detected during execution are called exceptions.

ex:
====
#File not found

with open("data.txt") as file:
    file.read()

result:
======
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
_________________________________


#Key error:

a_directory = {"key" : "value"}
print(a_directory["jdfjddadf"])

Results:
======
KeyError: 'jdfjddadf'

________________________________

#Index error

fruit_list = ["Banana", "Apple", "Mango"]
print(fruit_list[3])

Result:
======
IndexError: list index out of range
_____________________
#Type Error

text = "abc"
print(text + 123)

Results:
======
TypeError: can only concatenate str (not "int") to str
  
  6:13
    
