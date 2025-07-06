'''write a script for performing calculator operations of given two input numbers
1. addition
2. subtraction
3. multiplication
4. division
5. modulo %
6. square ( simple- /number ** 2)
3. cubic (number ** 3) ** means power of that number.
'''
# two input = addition = result needs to sqaure  and also cubic  of result

def addition_no(first_input:int,second_input:int) ->int:
    """
    Summation of two variable.

    args
    Input variable

    return
    Summation of two numbers
    
    """
    result_sum = first_input +second_input

    return result_sum

def subtracion_no(first_input:int,second_input:int) ->int:
    """
    Subtraction of two Numbers.

    args
    Input variable

    return
    Subtraction of two numbers.
    
    """  
    result_sub= first_input - second_input
    return result_sub


def multiplication_no(first_input:int,second_input:int) ->int:
    """
    Mutiplication of two Numbers.

    args
    Input variable

    return
    Mutiplication of two numbers.
    
    """  
    result_multi= first_input * second_input
    return result_multi

def division_no(first_input:int,second_input:int) ->int|float:
    """
    Division of two Numbers.

    args
    Input variable

    return
    Division of two numbers.
    
    """  
    result_div= first_input / second_input
    return result_div

def modulo_no(first_input:int,second_input:int) ->int:
    """
    Modulo of two Numbers.

    args
    Input variable

    return
    Modulo of two numbers.
    
    """  
    result_modulo= first_input % second_input
    return result_modulo

def square_no(first_input:int|float) ->int|float:
    """
    Square of the number.

    args
    Input variable

    return
    Square value of the number.
    
    """  
    result_square= first_input ** 2
    return result_square

def cube_no(first_input:int|float) ->int|float:
    """
    Cubic value of the number.

    args
    Input variable

    return
    Cubic value of the number.
    
    """  
    result_cube= first_input ** 3
    return result_cube

# Quation - two input = addition = result needs to sqaure  and also cubic  of result

# Define two variables
# calculate addition , calling funct addition_no
# store addition result in a sum_result 
# perform square value for result sum_result 
# perform cube value for result sum_result
# Print for quare and cube value of sum_result

# calculate subtraction  , calling funct subtraction_no
# store subtraction result in a sub_result 
# perform square value for result sub_result 
# perform cube value for result sub_result
# Print for quare and cube value

# calculate multiplication by calling function multiplication_no
# store multiplication result in a mult_result 
# perform square value for  mult_result 
# perform cube value for  mult_result
# Print for quare and cube result value mult_result

# calculate division by calling function division_no()
# store division result in a division_result 
# perform square value for  division_result 
# perform cube value for  division_result
# Print for quare and cube result value division_result


if __name__ == "__main__":  # this is the start of execution, above this is like as a reference and will be called inside this main func
    # Addition execution 
    input_first,input_sec= 4,3
    sum_result  = addition_no(input_first,input_sec)
    square_value_sum = square_no(sum_result)
    cube_value_sum  = cube_no(sum_result)
    print(f"Square value of Sum result = {square_value_sum}")
    print(f"Cube value of Sum result = {cube_value_sum}")

    # Subtraction execution 
    sub_result      =   subtracion_no(input_first,input_sec)
    square_value_sub=   square_no(sub_result)
    cube_value_sub  =   cube_no(sub_result)
    print(f"Square value of Sub result = {square_value_sub}")
    print(f"Cube value of  Sub result ={cube_value_sub}")

    # multiplication execution 
    mult_result         =   multiplication_no(input_first,input_sec)
    square_value_mult   =   square_no(mult_result)
    cube_value_mult     =   cube_no(mult_result)
    print(f"Square value of Multiplication result = {square_value_mult}")
    print(f"Cube value of  Multiplication result ={cube_value_mult }")

    # Division execution 
    division_result     =   division_no(input_first,input_sec)
    
    square_value_div   =   square_no(division_result)
    cube_value_div     =   cube_no(division_result)
    print(f"Square value of Division  result = {square_value_div:.2f}")
    print(f"Cube value of  Division result ={cube_value_div:.2f}")  #.2f will give ouptput  upto 2 decimal place value