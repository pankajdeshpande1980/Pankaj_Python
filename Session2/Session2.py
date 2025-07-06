x_name = 'Pankaj'
x_name1= x_name.replace('a','b')
x1_char = x_name[1]   #This is will give the second character of the string
print(f"{x1_char=}")

print(x_name)
print(x_name1)
'''
(method) def replace(
    old: LiteralString,
    new: LiteralString,  /,
    count: SupportsIndex = -1
) -> LiteralString
Return a copy with all occurrences of substring old replaced by new.
'''
# count
#     Maximum number of occurrences to replace.
#     -1 (the default value) means replace all occurrences.

# If the optional argument count is given, only the first count occurrences are
# replaced.

x3_count = x_name.count('a')    #string 
print(x3_count)
print(f"{x3_count=}")

x4_convert_low= x_name.lower()
print(f"{x4_convert_low=}")

x4_convert_upper= x_name.upper()
print(f"{x4_convert_upper=}")

x4_swap=x_name.swapcase()
print(f"{x4_swap=}")
# title 

# x_name = 'Pankaj'
chars=('p','P')  #Tuple
chars_end=('j','J') 
x5_check=x_name.startswith(chars)
print(x5_check)

x6_check_end=x_name.endswith(chars_end)
print(f"{x6_check_end=}")

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# python -m venv .venv


'''
print(f"{x6_check_end=}")
is an f-string (formatted string literal) introduced in Python 3.8.

How It Works:
The f before the quotes tells Python that it's a formatted string.
Inside the { } braces, the current_price= part is a special debugging syntax that:
Prints both the variable name (current_price) and
Its value (evaluated value of current_price).

Below are the list of of functions - 
replace()	    Replaces specific characters or substrings in a stock symbol, company name, or data string.
count()	        Counts the number of times a particular value or pattern appears in stock data.
lower()	        Converts stock symbols or company names to lowercase for uniform comparison.
upper()	        Converts stock symbols or company names to uppercase for uniform comparison.
swapcase()	    Swaps uppercase to lowercase and vice versa (useful for data formatting).
startswith()	Checks if a stock symbol or name starts with a specific prefix (useful in filtering).
endswith()	    Checks if a stock symbol or name ends with a specific suffix.

'''