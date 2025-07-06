list_1 = list(range(1, 100))

list_2 = []

# 1. iterate over every element from list_1
# 2. during iteration, add 1 to every element and store to a variable
# 3. Add that variable to the list_2

for element in list_1:                      # iterate over every element from list_1
    if element < 50:                        # check if the element is less than 50
        temp_value = element+1
        print(f"Actual value => {element}")
        print(f"incremented value => {temp_value}")
        
        list_2.append(temp_value)          # add the incremented value to list_2  
        print("=")
    else:
        print(f"the element is bigger than 50")
        break

print(list_2)

# list_3  = list(range(1,50))
# list_4   =[]            

# for element1 in list_3:
#     if (element1/3) or (element1/5):
#         temp_value1 = element1
#         list_4.append(temp_value1)
#         print("=")

#     else:
#         print(f"the element is divisible by 3 or 5")
    
# print(list_4)

list_3  = list(range(1,50))
list_4   =[]            

for element1 in list_3:
    if (element1/3 == element1) or (element1/5 == element1):
        temp_value1 = element1
        list_4.append(temp_value1)
        print("=")
        
    else:
        print(f"the element is divisible by 3 or 5")
    
print(list_4)

