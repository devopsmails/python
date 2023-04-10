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
33
12
7
4
72
2
42
13

file2.txt
=========
3
6
13
5
7
89
12
3
33
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

