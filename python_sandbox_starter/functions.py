# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name):
    print(f"hello {name}")
sayHello("John Doe")

# Return values
def getSum(num1,num2):
    x = num1+num2
    return x
print(getSum(3,5))
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getsum = lambda num1, num2 : num1 + num2
print(getsum(2,40))
