# Function definition part
# def function_name(*args, **kwargs):
# async (async def function_name(*args, **kwargs):) => async paradigm
# def => keyword to identify function
# function_name => name given for the function
# Naming should be in snake_case, no CamelCase, no ALLUPPERCASE
# args => arguments/parameters
# type hinting is mandatory
# kwargs => keyword agrguments/ keyword parameters
# docstrings => documentation


#Arithmatic functions
#1. Addition operation 
    # Define two input variable & one out put variable  and it's type and Operation + return 
#2. Subtraction operation 


def addition_two(var1:int |float,var2:int|float)-> int|float :  # text 
    '''Addition of two numbers

    Args : 
        var1(int|float): variable1
        var2(int|float): variable2
    Returns :
        int|float : Sum of two numbers 

    '''
      
    sum = var1+var2
    return sum

def subtraction_two(var1:int, var2:int)-> int|float:
    '''Subtraction of two numbers( this will identify the bigger number and then perform arithmatic operation)

    Args:
        var1(int)   :   variable1
        var2(int)   :   variable2

    Return
        int|float : Diffrence between two numbers.    
    
    '''
    if (var1 != var2):
        return max(var1, var2) - min(var1, var2)
    
    else :
        return 0


def multiplication_two(var1: int, var2: int) -> int:
    """multiplication of two given numbers

    Args:
        var1 (int): variable 1
        var2 (int): variable 2

    Returns:
        int: product of the two numbers
    """
    product = var1 * var2
    return product


def division_two(var1: int, var2: int) -> int:
    """division of two given numbers

    Args:
        var1 (int): variable 1
        var2 (int): denominator, should not be zero

    Returns:
        int: product of the two numbers
    """
    if var2 == 0:
        return "denominator should not be Zero"
    quotient = var1 / var2
    return quotient 

# print(f"subtraction_two(10, 5) = {subtraction_two(10, 5)}")     # Expected: 5
# print(f"subtraction_two(5, 10) = {subtraction_two(5, 10)}")     # Expected: 5
# print(f"subtraction_two(7, 7) = {subtraction_two(7, 7)}")       # Expected: 0
# print(f"subtraction_two(-3, 4) = {subtraction_two(-3, 4)}")     # Expected: 7
# print(f"subtraction_two(-5, -1) = {subtraction_two(-5, -1)}")   # Expected: 4

# def main():
#     input_list = list(range(1, 50))
#     result = count_odd_even_numbers(input_list)
#     print(result)
#     odd_numbers = count_odd_numbers(input_list)
#     even_numbers = count_even_numbers(input_list)
#     print(f"Number of odd numbers => {odd_numbers}, Number of even numbers => {even_numbers}")

if __name__ == "__main__":      # main statement
    # Addition execution 
    input_first,input_sec= 4,9
    sum_result  = addition_two(input_first,input_sec)
    diff_result = subtraction_two(input_first,input_sec)
    
    print(f"Sum result = {sum_result}")
    print(f"Subtraction result = {diff_result}")
