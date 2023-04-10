Dictionary Comprehension:
  ==============

dictionary comprehension offers a shorter syntax when you want to create a new dictionar based on the values of an existing dictionary.

syntax:
======
1. new_dict = {new_key : new_value for item in list}
2.  new_dict = {new_key : new_value for (key, value) in dict.items() if test}

import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)


challenges:
===========
Examples:

names = ["suresh", "Ramesh", " Kiran", "Ravi", "Manoj"]
#new_dict = {new_key : new_value for item in list}
import random
#dict_comprehension from list
new_dict = {student : random.randint(1,100) for student in names}
print(new_dict)

Result:
======
{'suresh': 70, 'Ramesh': 4, ' Kiran': 83, 'Ravi': 87, 'Manoj': 97}

#dict_comprehension from dict

new_dict_from_dict = {students : scores for (students, scores) in new_dict.items() if scores > 35}
print(new_dict_from_dict)

Result:
======
{'suresh': 70, ' Kiran': 83, 'Ravi': 87, 'Manoj': 97}
