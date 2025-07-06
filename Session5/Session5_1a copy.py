''' Create a program that counts and displays how many even and odd numbers exist between 1 and a number specified by the user using both loop types.'''
'''Write a pseudo code before writing any program'''

# Define input variable (get number from user) and convert it in int.
# Define two output variables: one for Even count, one for Odd count () List to store even numbers)
# Define iterator variable and set it to 1
# Start while loop with condition: iterator <= input number
    # Check if number is Even (number % 2 == 0)
        # If yes, increase Even count by 1
    # Else
        # Increase Odd count by 1
    # Increase iterator by 1
# After loop ends, print Even count  and Print Odd count (Use f-string)


input_no    = 10
input_no1    = int(input_no) # This is to convert the input number in Int 
Even_count  = 0             # Counter to track how many even numbers
Odd_count   = 0             # Counter to track how many odd numbers
i= 1 

while i<= input_no1 :
    if i%2 ==0:
        Even_count+=1
    else:
        Odd_count+=1
    i+=1
print( f" Total Even number count :- {Even_count}")
print( f" Total Odd number count :- {Odd_count}")


# print(f"Even numbers: {Even_no}")       # Display all even numbers
print(f"Even Count : {Even_count}")     # Display count of even numbers
# print(f"Odd numbers : {Odd_no}")        # Display all odd numbers
print(f"Odd Count : {Odd_count}")  

