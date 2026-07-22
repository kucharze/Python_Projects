print("Hello World")
print("I am learning Python programming")
print(12+8)#Prints a number
print("12+8")#Prints a string. Strings are always enclosed in quotes. You can use single or double quotes.

#Python can't split strings across multiple lines. You can use the backslash character to split a string across multiple lines. """ """

#Escape sequences are used to represent special characters in strings. For example, \n represents a new line, and \t represents a tab.
print("Hello World,\n I am learning Python programming")#Prints Hello World and I am learning Python programming on separate lines
print("Hello World,\t I am learning Python programming")#Prints Hello World and I am learning Python programming with a tab

# Comments are used to explain code and make it more readable. Comments are ignored by the Python interpreter. 
# You can use the # symbol to create a single-line comment, or triple quotes (""" """) to create a multi-line comment.
#The below print func prints Hellow world
print("Hello World") # This is a single-line comment

# print(12 + 90) # Prints the sum of 12 and 90

#Variables
#A container that stores data

x = 5 # Assigns the value 5 to the variable x
print(x)

acc=3467436767 # = is the assignment operator. It assigns the value on the right to the variable on the left.
print(acc)

print(12+8) # A Python statement is a line of code that performs an action. In this case, the statement adds 12 and 8 and prints the result.

#A more complex statement
if 12>45:
    print("12 is greater than 45")


#Data types
#Python will automatically assign a data type to a variable based on the value you assign to it.
# You can also explicitly specify the data type of a variable using type casting.
#Python has the following data types:
#Numbers
# - Integers
# - Floats

#Strings
#Booleans

a = 78
print(type(a))

b = "Hello"
print(type(b))

c = 12345.56
print(type(c))

#lists
#tuples
#sets
#dictionaries