# . Create a dictionary representing a person’s name and age.
person={"name":"Linn","age":24}
print(person)

# Access the age of the person from the dictionary above.
print(person["age"])

# Add a new key-value pair "city": "Nairobi" to the dictionary.
person["city"]="Nairobi"
print (person)

#  Check if the key "email" exists in the dictionary.
print("email"in person)

# Safely get the value of "email" without causing an error if the key is missing.
print(person.get("email"))

# Remove the "age" key from the dictionary.

del person["age"]
print(person)

# Iterate over all keys and print them.
for key in person:

    print(key)
# . Iterate over all values and print them.
for value in person:
    print(person.values())
# Iterate over key-value pairs and print them.
for key,value in person.items():
    print(f"{key}: {value}")

# Merge another dictionary {"email": "alice@example.com"} into person.
person.update({"email": "alice@example.com"})
print(person)

# Get the number of items in the dictionary.
print(len(person))

#  Clear all items from the dictionary.
person.clear()
print(person)

# Create a dictionary from two lists keys = ['a', 'b'] and values = [1, 2].
keys = ['a', 'b']
values = [1, 2]
d=dict(zip(keys,values))
print(d)

# Create a dictionary with default value 0 for keys 'x', 'y', 'z'.
keys=['x', 'y', 'z']
d=dict.fromkeys(keys,0)
print(d)

#  Safely remove a key 'phone' from the dictionary without raising an error.
print(person.pop("phone",None))

# Copy a dictionary.
person_copy=person.copy()
print(person_copy)

# Q17. Use a dictionary comprehension to square numbers from 1 to 3.

squares = {x: x*x for x in range(1, 4)}
print(squares)  

# Q18. Get a list of all keys in the dictionary.

keys_list = list(person.keys())
print(keys_list)

# Get a list of all values in the dictionary.
values_list=list(person.values())
print(values_list)

# Q20. Explain what happens if you try to access a missing key with person['phone'].
 Raises KeyError if 'phone' does not exist.
Use person.get('phone') to avoid error.















