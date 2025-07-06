''' Create a program that counts and displays how many even and odd numbers exist between 1 and a number specified by the user using both loop types.'''
# Define input variable (get number from user) and convert it to int
# Define two output variables: one for Even count, one for Odd count
# Start for loop from 1 to input number (inclusive)
    # Check if loop variable is Even (loop variable % 2 == 0)
        # If yes, increase Even count by 1
    # Else
        # Increase Odd count by 1
# After loop ends, print Even count and Odd count using f-strings



Input_n= int(input("Input number:-"))
list_1 = list(range(1, Input_n+1))              # This line creates a list of numbers starting from 1 up to n.////range(1, n+1) means: "Start from 1, and go up to n (including n)."
Even_no= []
Odd_no=[]
Even_count=0
Odd_count=0

for element in list_1:
    remaind_ev= element % 2
    if remaind_ev ==0:
        Even_count +=1
        Even_no.append(element)  # Append the cumulative sum to Even_no
    else:
        Odd_count +=1
        Odd_no.append(element)  # Append the cumulative sum to Even_no

print(f"Even numbers: {Even_no}")
print(f"Even Count : {Even_count}")
print(f"Odd numbers : {Odd_no}")
print(f"Odd Count : {Odd_count}")

  
