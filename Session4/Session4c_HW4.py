# 4. Create a program that prints the following pattern: 
# ``` 
#        * 
#        ** 
#        *** 
#        **** 
#        *****
# ```
Input_row = int(input("Enter a number = "))  # Take number of rows as input from the user

for element in range(1, Input_row + 1):      # Loop from 1 to Input_row (inclusive)
    stars = "*" * element                    # Create a string with 'element' number of stars
    # print(f"{stars.ljust(Input_row)}")     # Use f-string to print stars left-aligned to Input_row width
    print(f"{stars}") 