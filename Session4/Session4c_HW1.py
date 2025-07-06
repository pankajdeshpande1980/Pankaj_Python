# Write a program that calculates the sum of all numbers from 1 to n, where n is a number input

# Define input variable (get number from user) and convert it to int
# Define one output variable: sum = 0
# Start for loop from 1 to input number (inclusive)
    # Add loop variable to sum
# After loop ends, print the sum using f-string


Input_n = int(input("Input number: "))  # Correctly get user input
# Input_n = (input("Input number: "))       # Correctly get user input6
list_1 = list(range(1, Input_n+1))        # This line creates a list of numbers starting from 1 up to n.////range(1, n+1) means: "Start from 1, and go up to n (including n)."
list_2 = []

# Variable to store cumulative sum
sum = 0

# Calculate the cumulative sum and store it in list_2

for element in list_1:
    sum = sum+element       # Update the sum by adding the current element
    list_2.append(sum)      # Append the cumulative sum to list_2

# Print the list of cumulative sums
print(list_1)
print(list_2)
print(sum)
