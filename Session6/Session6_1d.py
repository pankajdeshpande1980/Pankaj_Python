''' 3. Write a program that calculates the factorial of a number (n!) using both loop types. Example: 5! = 5 × 4 × 3 × 2 × 1 = 120 '''
# 
# Define a variable for For loop result, set it to 1
# Start For loop: from 1 to input number (inclusive)
    # Multiply the for_loop_result by the current element
# print the factorial calculated using For loop (use f-string)
# Return factorial values 


def factorial_number(input_number: int) -> int:
    """
    Calculate the factorial of a given number using both for loop and while loop.

    args
    ----
    input_number: int => The number for which the factorial will be calculated

    returns
    -------
    for_loop_result: list[int, int] => Factorial calculated using for loop.
    """

    # Using for loop
    factorial_result = 1
    for element in range(1, input_number + 1):
        factorial_result *= element
          
    print(f"Factorial of {input_number} is = {factorial_result}")
    
    return factorial_result

factorial_final_result = factorial_number(3)
print(f"Factorial  = {factorial_final_result}")