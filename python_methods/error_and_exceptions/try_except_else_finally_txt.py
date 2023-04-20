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
type: 2
=======

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass #pass it to the next line of code if it finds the same error

print(total_likes)
