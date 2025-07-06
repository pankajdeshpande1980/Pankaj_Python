# # Variables
# my_name = "Santhosh"
# my_age = 18

# # dynamic typed
# # static typed
# my_age = 18


# datatypes
# 1. string        
my_name = "Santhosh"
print(type(my_name))
# print(my_name.upper())

# 2. Int
my_age = 31
print(type(my_age))

# 3. Boolean
am_i_old = True
print(type(am_i_old))

# 4. Nonetype - Default data type
whatever = None # null
print(type(whatever))

# 5. List (mutable arrays)
python_int_list = [1, 2, 3, 3]
python_str_list = ["a", "b", "c"]
python_list = [1, "b", True]
print(type(python_int_list))
print(type(python_str_list))
print(type(python_list))


# 6. tuples (immutable array).( reference data from outside is always same) 
python_tuples = (1, 2, 3)
print(type(python_tuples))

# 7. dictionary (hash tables)
indian_states = {"Maharashtra": "Mumbai", "Tamil Nadu": "Chennai"}
mixed_dicts = {"numbers": [1, 2, 3], 2: ("a", "r")}

# 8. set
set_example = set([1, 3, 4, 4])
print(set_example)
print(type(set_example))
set_example


'''
Operators in Python
Operators are used to perform mathematical and logical operations.
'''
# ==            => is equal to
# >=            => greater than or equal to
# <=            => lesser than or equal to
# <             => lesser than
# >             => greater than
# !=            => not equal to
# %             => is used to get remainder value 

# scope - indentation
# control statement

if my_name == "Santhos":
    print("yes")
    print("yes")
    print("yes")
    print("yes")
elif my_name == "Santhosh":
    print("second check")
else:
    print("no")
    print("yes")
    print("yes")
    print("yes")



