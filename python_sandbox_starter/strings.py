# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Brad"
age  = 37
#Concatener
print("hello, my name is " + name)
print("helle my name is " + name + " and " +  str(age))
# String Formatting
# Arguments by position
print("My name is {name} and I am {age}".format(name=name, age=age))
#F-Strings
print(f"Hello, my name is {name} and I am {age}")
# String Methods
s = "hello world"
#Capitalize string
print(s.capitalize())
# make all uppercase
print(s.upper())
# Make all lower
print(s.lower())
# swap case
print(s.swapcase())
# Get lenght
print(len(s))
# Replace
print(s.replace("world", "everyone"))
# starts with
print(s.startswith(("bonjour")))
print(s.startswith(("hello")))
# Ends with
print(s.endswith(("d")))
# Split into a list
print(s.split())
print(s.split(","))
# Find position
print(s.find("r"))
# is all alphanumeric
print(s.isalnum())
# is all alphabetic
print(s.isalnum())
# is all numeric
print(s.isnumeric())
