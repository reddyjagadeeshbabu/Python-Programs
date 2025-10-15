#variables are containers it can stores the vlaues.
"""
a=143
b="jagadhee"
print(a,b)
"""
""""
#Single or Double Quotes?
#String variables can be declared either by using single or double quotes:
a="john"
a='john'
print(a)
"""
"""
#Get the Type
#You can get the data type of a variable with the type() function.
a=54
b="jagadhee"
print(type(a))
print(type(b))
"""
"""
#identifiers

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
"""
"""
#assign multiple variables
x,y,z="orange","green","bananna"
print(x,y,z)

"""
"""
#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
x=y=z="orange"
#print(x,y,z)
print(x)
print(y)
print(z)

"""
"""
#Unpack a Collection
fruits=["bananna","mango","green"]
x,y,z=fruits
print(x,y,z)

"""
