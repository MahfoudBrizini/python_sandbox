# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dict
person = {
    "first_name":"John",
    "last_name": "Doe",
    "age": 30
}
print(person, type(person))
# use constroctor
person2 = dict(first_name = "Sara", last_name = "Williams")
print(person2, type(person2))
# Get value
print(person["last_name"])
print(person.get("last_name"))
# Add key/value
person["phone"] = "555-555-5555"
print(person)
# get all keys
print(person.keys())
# get all items
print(person.items())
# copy dict
pap2 = person.copy()
pap2["city"] = "boston"
print(pap2)
# remove an item
del(person["age"])
print(person)
person.pop("phone")
print(person)
# clear
person.clear()
print(person)
# Get len
print(len(pap2))

# list of dict
people = [
    {"name":"Martha", "age":30},
    {"name":"Kevin", "age":25}
]
print(people,type(people))
print(people[1]["name"])