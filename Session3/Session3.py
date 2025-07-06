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
list_1.insert(0, 99)      # this will insert 99 at the beginning of the list
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


# Append, Insert, Extend, Remove, Pop, Count, Index, Sort, Reverse
# List operations.

'''# Dictionary operations
# Dictionary operations.
# 1. How to create a dictionary? 
# 2. How to add elements to a dictionary?
# 3. How to remove elements from a dictionary?
# 4. How to access elements from a dictionary?
# 5. How to update elements in a dictionary?
# 6. How to iterate through a dictionary?
# 7. How to check if a key exists in a dictionary?  
# 8. How to get the length of a dictionary?
# 9. How to clear a dictionary?
# 10. How to copy a dictionary?
# 11. How to merge two dictionaries?
# 12. How to get the keys and values of a dictionary?
# 13. How to get the items of a dictionary?
# 14. How to get the keys of a dictionary?'''