# ABS Character Picture Grid pg: 103
# Day 4 of 100

'''make this look like:

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....


Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will fin- ish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].
Also, remember to pass the end keyword argument to print() if you don?t want a newline printed automatically after each print() call.

'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


col_range = len(grid[0]) # 6 [0-5], defines column length grid[0]
row_range = len(grid)    # 9 [0-8], when you loop through rows are what you see so grid is row range

"""IN WORDS WHAT I HAD TO FIGURE OUT

started with seeing how things worked with the rows:

for x in range(0, row_range):
    print(grid[x])

and thought how to make the rows columns so i wanted to see how to manipulate the output of the columns or what that looked like.  Since there are only 6 columns, the range only goes 6 rounds, meaning when you call grid[y].  You dont account that you need y as the second character

for y in range(0, col_range):
    print(grid[y])

that really did nothing to help.

So i need to make the row length as columns and columns as rows.  Since we iterate over rows, that has to be on the outside.  so i moved columns to the outside

then it was about formatting the output.  i used a join to join all the elements of the list.

since end="" is a way get rid of new line, how could i get it to flip at the appropriate time.  So far everything just looked like:

Clue 100daysofpython # python3 ABS-CharacterPictureGrid.py 
. . O O . O O . . . O O O O O O O . . O O O O O O O . . . O O O O O . . . . . O O O . . . . . . . O . . . . Clue 100daysofpython # 

so i still couldn't figure out the new line.  I added the new line AFTER the print statemnt of the join and nothing.  then...i tabbed back 1, and boom!

this is VERY much an area i need to work on.

"""

for y in range(0, col_range):
    for x in range(0, row_range):
        line = ''.join(grid[x][y])
        print(line, end=" ")
    print('\n')



