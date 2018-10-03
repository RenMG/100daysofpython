#Automate the Boring Stuff: Pg 77: The Collatz Sequence practice
#Issues run into was with git and variables, but over all things went smooth.
#Day 2 of 100 days of code

def collatz(number):
    result_num = number % 2    # == 1 odd / 0 even
    if result_num == 1:
        odd_calc = 3 * number + 1
        print('Odd Number: {0}').format(odd_calc)
        return odd_calc
    elif result_num == 0:
        even_calc = number /  2
        print('Even Number: {0}').format(even_calc)
        return even_calc
    else:
        print('not a fucking number')

print('Give me an integer: ')
try:
    input_num = int(input())
except NameError:
    print('Error: Please enter a number')


while input_num != 1:
    print('Current calc: {0}').format(input_num)
    input_num = collatz(input_num)