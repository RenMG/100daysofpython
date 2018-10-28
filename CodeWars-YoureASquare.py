def is_square(n):  
    squared = n**(.5)
    if(n < 0):
        return False
        raise Exception('{}: Negative numbers cannot be square numbers'.format(n))
    elif(squared.is_integer()):
        if(squared*squared == n):
            print(True)
            return True
    else:
        print(False)
        return False

is_square(20391820831)

# The big learn here was taking the square root.  n**.5 silly way, but good to know.  the outter if/else are to validate the number is useful, the innter is to validate a qualified number is squared.