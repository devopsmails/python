Try     : Something that might cause an exception
except  : Do this if there was an exception
else    : Do this if there was no exception
finally : Do this no matter what happens
raise   : We can raise our own exceptions(errors). 
          No matter eceptions(errors) occurs or not should raise this exception. 
          Ex:
          height= float(input("Height(Mtrs): "))
          weight= float(input("Weight(Kg): "))

          bmi = height / weight ** 2
          if height > 3:
              raise ValueError("Human height should not be over 3 meters")
          print(bmi)
   
______________________________________________
  
Examples:
=======

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    raise TypeError("This is my own created error") 
    
Results:
========
TypeError: This is my own created error
value
something
File was closed

--------------
