''' Problem 1- convert the input value-  celsius_to_fahrenheit(celsius)
    Problem 2- convert the input value-  fahrenheit to celsius(fahrenheit)
'''

#define function 
#input variable and type , output variable in type
#perform arithmatic calculation for C to F
#return (output)

def celsius_fer(celsius_input:int|float) -> int|float:
    """
    Convert the celsius value to fahrenheit unit

    Args : 
    celsius_input(int|float) : Input value in celsius

    Return :
        int|float : Converted value from CElsius to fahrenheite.
            
    """
    fahrenhite_value= (celsius_input * 9/5) + 32 

    return fahrenhite_value

# var1= 33
# var2= celsius_fer(var1)
# print(f"fahrenhite value = {var2} ")

def fahrenhite_celsius(fahrenhite_input: int|float)-> int|float :
    """
    Convert the fahrenheit value to celsius value unit

    Args : 
    fahrenhite_input(int|float) : Input value in fahrenhite

    Return :
        int|float : Converted value from  to fahrenheite to Celsius.
       
    """
    celsius_value  = (fahrenhite_input-32) * 5/9
    return celsius_value

var3    =100
var4    =fahrenhite_celsius(var3)
print(f"fahrenhite value :{var4:.2f}")   # this is to restrict decimal value.




# 1. Problem statement 
# 2. Psedo code 
# 3. functions 
# 3.