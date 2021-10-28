# A List is a collection which is ordered and changeable. Allows duplicate members.
# just like array
# Create a list
numbers = [1,2,3,4,5]
fruits = ["Apple", "Oranges", "Grapes", "Pears"]
# use a constroctor
numbers2 = list((1,2,3,4,5,5))
print(numbers,numbers2)
# get a single value
print(fruits[0])
print(fruits[1])
# get a len of a list
print(len(fruits))
# Append to list
fruits.append("Mangos")
print(fruits)
# Remove
fruits.remove("Grapes")
print(fruits)
# insert into position
fruits.insert(1,"mahfoud")
print(fruits)
# change value
fruits[0] = "Blueberries"
# remove with pop
fruits.pop(1)
print(fruits)
#reverse
fruits.reverse()
print(fruits)
# sort alphabeticly
fruits.sort()
print(fruits)
# reverse sort
fruits.sort(reverse = True)
print(fruits)