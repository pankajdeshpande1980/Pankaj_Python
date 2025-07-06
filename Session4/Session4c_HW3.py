''' 3. Write a program that calculates the factorial of a number (n!) using both loop types. Example: 5! = 5 × 4 × 3 × 2 × 1 = 120 '''

Input_n = int(input("Enter a number = "))   # Take number input from user
list_2 = []                                 # Empty list to store numbers used in factorial

factorial = 1                               # Initialize factorial result to 1
element = 1  
for element in range(1, Input_n+1):         # Loop from 1 to Input_n (inclusive)
    factorial *= element                    # Multiply factorial by current element
    list_2.append(element)                  # Add current element to the list



# while element <= Input_n:                   # Run loop until element reaches Input_n
#     factorial *= element                    # Multiply factorial by current element
#     list_2.append(element)                  # Add current element to the list
#     element += 1                            # Move to next number


print(f"Numbers used for factorial: {list_2}")  # Show the sequence of numbers multiplied
print(f"Factorial of {Input_n} using for loop is: {factorial}")  # Display result

