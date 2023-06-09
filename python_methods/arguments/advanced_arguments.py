#Arguments with Default values:
=====================

def my_function(a=1,b=2,c=3):
 
#calling the function with default values:
  
my_function()

# Edit the default arguments for custom purpose:
my_function(b=5)

=============

#Unlimited Arguments:
================

 => need to use "*args" to use unlimited arguments feature.
 
Example:
 
def add(*args):
 
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2,3, 4, 6, 9, 7))

Result:
===

32
=============
# Unlimited Positional Arguments:
=============
def add(*args):
    #unlimited with positional arguments
    print(args[4])
    
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2,3, 4, 6, 9, 7))

Result:
=====

#Postional arg = 
6
#sum
32

# Key word argument (**kwargs):
=========================
 ==> Need to have two "**kwargs" in function.
 
 #Type 1:
 ======
 
 def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add =2, multiply=5)

Results:
=======

add
2
multiply
5

#Type 2:
=======
#Custom Value for a key:
def calculate(n, **kwargs):
 
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add =3, multiply=5)

Result:
=======

{'add': 3, 'multiply': 5}
25
