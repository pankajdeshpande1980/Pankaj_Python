'''The print() function in Python works with all data types and outputs them as a string representation to the console.
You can print individual data types or combine them using f-strings, str.format(), or direct concatenation.
print(f"{Int_x = }")
print(f"{x6_check_end=}")
is an f-string (formatted string literal) introduced in Python 3.8.

How It Works:
The f before the quotes tells Python that it's a formatted string.
Inside the { } braces, the current_price= part is a special debugging syntax that:
Prints both the variable name (current_price) and
Its value (evaluated value of current_price).

'''

# Int 
Int_x = 10
print(Int_x)  # Direct printing
print(f"{Int_x = }")
print(f"Price  = {Int_x}")  # Using f-string
print("Int_x1 =", Int_x + 10 +(10*2))  # Using comma separation
print("Int_x3 = {}".format(Int_x))  # Using format()
# print(f"{Int_x = }")


stock_ticker = 'AAPL'
price = 226.41
print('We are interested in {x} which is currently trading at {y}'.format(x=stock_ticker, y=price))

print('We are interested in {} which is currently trading at {}'.format(stock_ticker, price))
