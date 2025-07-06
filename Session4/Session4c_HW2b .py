''' Create a program that counts and displays how many even and odd numbers exist between 1 and a number specified by the user using both loop types.'''
# Define input variable (get number from user) and convert it to int
# Define two output variables: one for Even count, one for Odd count
# Define iterator variable and set it to 1 
# Start while loop with condition: iterator <= input number
    # Check if iterator is Even (iterator % 2 == 0)
        # If yes, increase Even count by 1
    # Else
        # Increase Odd count by 1
    # Increase iterator by 1
# After loop ends, print Even count and Odd count using f-strings


Input_n = int(input("Input number: "))  # Take user input and convert it to an integer

Even_no = []         # List to store even numbers
Odd_no = []          # List to store odd numbers
Even_count = 0       # Counter to track how many even numbers
Odd_count = 0        # Counter to track how many odd numbers

element = 1          # Start checking from number 1

while element <= Input_n:               # Keep running loop until we reach the input number
    if element % 2 == 0:                # % operator gives remainder; if 0, number is even
        Even_count += 1                 # Add 1 to even counter
        Even_no.append(element)         # Store the even number in the list
    else:
        Odd_count += 1                  # Add 1 to odd counter
        Odd_no.append(element)          # Store the odd number in the list
    element += 1                        # Move to the next number

# Print results using f-strings
print(f"Even numbers: {Even_no}")       # Display all even numbers
print(f"Even Count : {Even_count}")     # Display count of even numbers
print(f"Odd numbers : {Odd_no}")        # Display all odd numbers
print(f"Odd Count : {Odd_count}")       # Display count of odd numbers