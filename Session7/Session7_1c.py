def count_even_numbers(input_list: list[int]) -> int:
    counter = 0
    for element in input_list:
        if element % 2 == 0:
            counter += 1
    return counter

def count_odd_numbers(input_list: list[int]) -> int:
    counter = 0
    for element in input_list:
        if element % 2 != 0:
            counter += 1
    return counter

def main():
    input_list = list(range(0, 50))
    odd_count = count_odd_numbers(input_list)
    even_count = count_even_numbers(input_list)
    print(f"Number of Odd Numbers => {odd_count}")
    print(f"Number of Even Numbers => {even_count}")

if __name__ == "__main__": # this is the start of execution, above this is like as a reference and will be called inside this main func
    main()

 