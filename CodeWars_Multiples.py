# Playing around with CodeWars cuz i wanted to play elsewhere and not some textbook thing
# Day 7 of 100

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

def multiples(number):
    check = str.isalpha(str(number))

    if(check == True):
        print('please input a real number')
    else:
        count = 0
        for x in range(number):
            #lesson learned: Can't put this into a condition.  Must section as a var :)
            multiple_3 = x % 3
            multiple_5 = x % 5
            if(multiple_3 == 0):
                count = count + x
            elif(multiple_5 == 0):
                count = count + x
            else:
                pass  
        #codewars requires this be a return, but here i can't get to show with a return
        print(count)
        return count

multiples(10)