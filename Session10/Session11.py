#count the number of letters in a string
#define input for the string 
#Define one initiator
#define function 
#(**doc string :- definition :arg ststement:retrun statement)
    #define variable and type  for input and output
    #Define iterator ,counter
    #for loop for Element of input variable
    #Increase counter by +1
#Return  statemet to complete the function.


def count_letter(var1:str)->int :
    """
    Count the number of letters in a input string

    Args : 
    var1(str)   :variable1 
    
    Return :
        int: the total numbers of letter in string.
    
    """
    counter=0  

    for element in var1:
        counter +=1

    print(f"Number of letters-1 :{counter}")    
    return counter
var1 = "PankajDeshpande"
var2 = count_letter(var1)
print(f"Number of letters-2:{var2}")