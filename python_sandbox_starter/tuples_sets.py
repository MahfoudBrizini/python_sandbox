# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create a tuple
fruits = ("Apple", "Oranges", "Grapes")
fruits = tuple(("Apples", "oranges", "Grapes"))
print(fruits)

fruits2 = ("Apple")
print(fruits2, type(fruits2))
fruits2 = ("Apple",) # single values needs trailing comma
print(fruits2, type(fruits2))
#get Value
print(fruits[1])
#fruits[0] = "Pears" cannot operate
#del fruits
print(fruits)

# len
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create set
fruits_set = {"Apples", "Oranges", "Mango"}
# Check if in set
print("Apples" in fruits_set)
# add to set
fruits_set.add("Graperinos")
fruits_set.add("Apples")
print(fruits_set)
# remove
fruits_set.remove("Graperinos")
print(fruits_set)
# clear
fruits_set.clear()
print(fruits_set)