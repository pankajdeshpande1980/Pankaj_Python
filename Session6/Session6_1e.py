''' 3. Write a program that calculates the factorial of a number (n!) using both loop types. Example: 5! = 5 × 4 × 3 × 2 × 1 = 120 '''
# Define input variable (get number from user) and convert it to int
# Define a variable for While loop result, set it to 1
# Define a counter variable and set it to 1
# Start While loop with condition: counter <= input number
    # Multiply the while_loop_result by the counter
    # Increase the counter by 1
# Print the factorial calculated using While loop (use f-string)
# Return both factorial 

def factorial_number_while(input_number: int) -> int:
    """
    Calculate the factorial of a given number using a while loop.

    args
    ----
    number: int => The number for which the factorial will be calculated

    returns
    -------
    factorial_result: int => Factorial calculated using while loop
    """

    # Using while loop
    factorial_result = 1
    element= 1
    while element <= input_number:                   
        factorial_result *= element                   
        element += 1                                   
      
    print(f"Factorial of {input_number} is = {factorial_result}")
    return factorial_result

factorial_final_result = factorial_number_while(3)
print(f"Factorial  = {factorial_final_result}")