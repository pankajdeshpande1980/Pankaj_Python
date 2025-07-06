''' Create a function  that counts and displays how many even and odd numbers exist between 1 and a number specified by the user using both loop types.'''
# def => keyword to identify function
# function_name => name given for the function
# example= def function_name(*args, **kwargs):
# Naming should be in snake_case, no CamelCase, no ALLUPPERCASE
# args => arguments/parameters
# type hinting is mandatory
# kwargs => keyword agrguments/ keyword parameters
# docstrings => documentation
#  
# Define input variable (get number from user) and convert it to int
# Define two output variables: one for Even count, one for Odd count
# Start for loop from 1 to input number (inclusive)
    # Check if loop variable is Even (loop variable % 2 == 0)
        # If yes, increase Even count by 1
    # Else
        # Increase Odd count by 1
# After loop ends, print Even count and Odd count using f-strings

# Function wrtting 
def count_even_odd(input_end_point: int) ->list[int,int]:
    """
    Count and display how many even and odd numbers exist between 1 and a given number using For loop type.

    args
    ----
    input_end_point: int => The number up to which even and odd numbers will be counted (inclusive)

    returns
    -------
    even_count, odd_count: list[int, int] => A list containing counts of even and odd numbers
    """

    even_count = 0
    odd_count = 0
    for number in range(1, input_end_point + 1):
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"For Loop :- Even Count= {even_count}, Odd Count= {odd_count}")  # This is not required 

    return [even_count, odd_count]

even_result, odd_result = count_even_odd(7)
# print(f"Even Count: {even_result}, Odd Count: {odd_result}")
