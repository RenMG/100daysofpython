# ABS- Organized TableData.  Page: 143
# ***DOESN'T COUNT CUZ I HAD TO FIND THE ANSWER AND DISSECT TO UNDERSTAND
# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
def printTable(table):
    """
    THIS WAS PART OF THE PULLED SOLUTION...IT ADDS NO VALUE TO THE ACTUAL FUNCITON
    # create a new list of 3 "0" values: one for each list in tableData
    # colWidths = [0] * len(table)
    # search for the longest string in each list of tableData
    # and put the numbers of characters in the new list
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)
    """
    # THIS IS THE GOOD STUFF...
    # "rotate" and print the list of lists
    for x in range(len(table[0])) :
        for y in range(len(table)) :
            print(table[y][x].rjust(8), end = ' ')
        # THIS IS A GOTCHA...IF YOU MOVE THIS PRINT STATEMENT AROUND YOU GET A VARIATY OF OUTPUT VARIATION.
        print()

printTable(tableData)

'''
table_col = len(tableData[0])   # 4 columns
table_row = len(tableData)      # 3 rows

tableLength = {}

for y in range(table_col):
    for x in range(table_row):
        tableData.sort(key=len)    
        var = tableData[x][y]
        length = 0
        word_len = len(var)
        tableLength[var] = word_len
print(tableLength)

for key, value in tableLength.items():
    print(str(key).rjust(10), value)
    
'''