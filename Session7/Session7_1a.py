

def count_even_numbers(input_list: list[int]) -> int:
    """
    Count the number of even numbers in a given list of integers.

    args
    ----
    input_list: list[int] => A list containing integer elements to be checked for even numbers

    returns
    -------
    counter: int => Total number of even numbers found in the input list
    """
    counter = 0
    for element in input_list:
        # print(f"current element =>{element}")
        if element % 2 == 0:
            counter+=1

    return counter

def count_odd_numbers(input_list: list[int]) -> int:
    """
    Count the number of odd numbers in a given list of integers.

    args
    ----
    input_list: list[int] => A list containing integer elements to be checked for odd numbers

    returns
    -------
    counter: int => Total number of odd numbers found in the input list
    """
    counter = 0
    for element in input_list:
        if element % 2 != 0:
            counter+=1

    return counter

def count_odd_even_numbers(input_list: list[int]) -> dict[str, int]:
    """
    Count the number of odd and even numbers in a given list of integers.

    args
    ----
    input_list: list[int] => A list containing integer elements to be checked for odd and even numbers

    returns
    -------
    result: dict[str, int] => A dictionary with counts of odd and even numbers.
                              Example: {"odd_numbers": 25, "even_numbers": 25}
    """
    odd_counter, even_counter = 0, 0
    for element in input_list:
        if element % 2 == 0:
            even_counter+=1
        elif element % 2 != 0:
            odd_counter+=1

    return {"odd_numbers": odd_counter, "even_numbers":even_counter}


# def main():
#     input_list = list(range(1, 50))
#     result = count_odd_even_numbers(input_list)
#     print(result)
#     odd_numbers = count_odd_numbers(input_list)
#     even_numbers = count_even_numbers(input_list)
#     print(f"Number of odd numbers => {odd_numbers}, Number of even numbers => {even_numbers}")

# def main():
# Step 1: Create a sample list of numbers
input_list = list(range(0, 50))  # You can change the range as needed

# Step 2: Call the odd/even functions
Input_n = int(input("Input number: "))
if (Input_n== 2):
    odd_count = count_odd_numbers(input_list)
    even_count = count_even_numbers(input_list)
# Step 3: Print the result
    print(f"Number of Odd Numbers => {odd_count}")
    print(f"Number of Even Numbers => {even_count}")