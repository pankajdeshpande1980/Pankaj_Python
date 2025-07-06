
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
    remainder = element1%3  # % is used to get remainder value 
    remainder2 = element1%5
    if remainder ==0 or remainder2 ==0: 
        temp_value1 = element1
        list_4.append(temp_value1)
        print("=")
        
    else:
        print(f"the element is divisible by 3 or 5 ")
    
print(list_4)


