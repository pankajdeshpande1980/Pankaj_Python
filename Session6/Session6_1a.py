'''Calculate the cumulative sum of numbers between two integers'''
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

'''Calculate the cumulative sum of numbers between two integers'''
def cumulative_sum_of_n_elements(start_point: int, end_point: int) -> int:
    """
    Calculate the cumulative sum of numbers between two integers.

    args
    ----
    start_point: int => Starting point of a range to sum
    end_point: int => End point of a range to sum

    returns
    -------
    sum: int => sum of the numbers between starting_point and end_point

    """

    range_of_numbers = range(start_point, end_point+1)
    # print(range_of_numbers)

    sum = 0
    for i in range_of_numbers:              # for loop to iterate through the range of numbers
        # print(f"current element => {element=}")
        sum+=i
        # print(f"Current value of sum => {sum=}")

    return sum

result = cumulative_sum_of_n_elements(5, 6)
print(result)
print(f"Cumulative Sum: {result}") 




# def cumulative_sum_of_n_elements(start_point: int, end_point: int) -> int:
#     range_of_numbers = range(start_point, end_point+1)
#     sum = 0
#     for i in range_of_numbers:              # for loop to iterate through the range of numbers
#         sum+=i
    
#     return sum


# result = cumulative_sum_of_n_elements(5, 6)
# print(f"Cumulative Sum: {result}")
