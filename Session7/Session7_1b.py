import sample # module import
from sample import count_even_numbers
import time
import timeit

input_list = list(range(0, 1000))
# result = count_odd_even_numbers(input_list)
# print(result)

# start_time = time.time()
even_numbers = count_even_numbers(input_list)
# end_time = time.time()
# even_numbers_calc_time = end_time - start_time
# print(f"Time taken for calculating even numbers => {even_numbers_calc_time:.6f}")


start_time = time.time()
odd_numbers = sample.count_odd_numbers(input_list)
end_time = time.time()
# odd_numbers_calc_time = end_time - start_time
# print(f"Time taken for calculating odd numbers => {odd_numbers_calc_time:.6f}")


print(f"Number of odd numbers => {odd_numbers}, Number of even numbers => {even_numbers}")

time_taken_even = timeit.timeit(f"count_even_numbers({range(0,100)})", setup="from sample import count_even_numbers", number=100)
print(f"Time taken for calculating even numbers => {time_taken_even:.6f}")

time_taken_odd = timeit.timeit(f"count_odd_numbers({range(0,100)})", setup="from sample import count_odd_numbers", number=100)
print(f"Time taken for calculating odd numbers => {time_taken_odd:.6f}")
