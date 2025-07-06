"""
15-3-2025
1. List operations
2. Dictionary operations
3. Loops
    1. For
    2. While
"""

# List operations
list_1 = [] # empty list instantiation - preferred
list_2 = list() # empty list instantiation 

# checking number of elements in a list
list_1_length = len(list_1)
print(f"Length of the list_1 is {list_1_length=}")

# adding elements to list

# append
list_1.append(1)
print(f"list_1 => {list_1}")

list_1.append(2)
print(f"list_1 => {list_1}")

value_3 = "3"
list_1.insert(0, 99)
list_1.insert(2, 100)
print(f"list_1 => {list_1}")


list_3 = [4, 5]
# list_1 => [1, 2, '3', 4, 5]
# list_1.append(list_3)
# print(f"list_1 => {list_1}")

# extend
list_combined = list_1+list_3
print(f"list_combined => {list_combined}")
print(f"list_1 => {list_1}")

list_1.extend(list_3)
print(f"list_1 => {list_1}")

# identification of elements

count_element = list_1.count(1)
print(f"Number of occurrence of 1 in list_1 => {count_element}")
list_1.extend(["a", 1, "a"])
print(f"list_1 => {list_1}")
count_element = list_1.count("A")
print(f"Number of occurrence of a in list_1 => {count_element}")

search_element = "a"
index_location = list_1.index(search_element)
print(f"Location of {search_element} is {index_location}")


# removing elements from list
list_1.remove("a")
print(f"list_1 => {list_1}")

third_element = list_1.pop(3)
print(f"The third element is {third_element}")

# checking number of elements in a list
list_1_length = len(list_1)
list_length_check = f"Length of the list_1 is {list_1_length=}"
print(list_length_check)

# ordering operations
list_1.remove("a")
print(f"list_1 => {list_1}")

list_1.sort()
print(f"Ascending order of list_1 => {list_1}")
list_1.sort(reverse=1)
print(f"Descending order of list_1 => {list_1}")

list_1.reverse()
print(f"Reversed list_1 => {list_1}")

list_1.clear()
print(f"Cleared list => {list_1}")

# Dictionary operations

# template of dictionary => {"key1":"value1", "key2":"value2",...}

person = {
    "name": "Pankaj Deshpande",
    "age": 40,
    "employed": True,
    "experience": ["XYZ", "ABC"],
    "marital status": True,
    20: {"test": "test"}
}

# get items from dictionary
keys_from_dict = person.keys()
print(f"Type of keys_from_dict => {type(keys_from_dict)}")
print(f"Keys from dictionary => {keys_from_dict}")

values_from_dict = person.values()
print(f"Type of values_from_dict => {type(values_from_dict)}")
print(f"values from dictionary => {values_from_dict}")

name_of_person = person["name"]
print(f"Name of the person is {name_of_person}")

name_of_person = person.get("name")
print(f"Name of the person is {name_of_person}")

citizenship = person.get("citizenship", "Indian")
print(f"Citizenship of the person is {citizenship}")

# manipulation of the dictionary
person["age"] = 41
print(f"Updated dictionary => {person}")

person["experience"] = {"first_job" : "XYZ", "second": "ABC"}
print(f"Updated dictionary => {person}")

# add one more entry/elemnt/key-value pair to a dict
person.update({"additional_info" : "learning Python"})
print(f"Updated dictionary => {person}")

# pop items
popped_item = person.popitem()
print(f"Popped item => {popped_item}")

popped_value = person.pop("name")
print(f"Popped key => {popped_value}")

print(f"Updated dictionary => {person}")

# clear 
person.clear()

print(f"Cleared dictionary => {person}")
