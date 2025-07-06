# Create a function  that counts and displays how many even and odd numbers exist between 1 and a number specified by the user using both loop types.Use variable =  even_count=0 , odd_count=0 and function name = count_even_odd
def count_even_odd(input_end_point: int) -> tuple[int, int]:
    """
    Count and display how many even and odd numbers exist between 1 and a given number using both loop types.

    args
    ----
    input_end_point: int => The number up to which even and odd numbers will be counted (inclusive)

    returns
    -------
    even_count, odd_count: tuple[int, int] => A tuple containing counts of even and odd numbers

    """

    # Using for loop
    even_count = 0
    odd_count = 0
    for number in range(1, input_end_point + 1):
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"From For Loop :- Even Count = {even_count}, Odd Count = {odd_count}")

    # Reset counters for while loop display
    even_count = 0
    odd_count = 0
    number = 1

    # Using while loop
    while number <= input_end_point:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number += 1

    print(f"While Loop :- Even Count = {even_count}, Odd Count = {odd_count}")

    return even_count, odd_count

even_result, odd_result = count_even_odd(6)
print(f"Even Count: {even_result}, Odd Count: {odd_result}")