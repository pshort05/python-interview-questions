"""""
Question

This problem is inspired by Minecraft. To craft things from raw material, you are given a 2 x 2 or 3 x 3 cell matrix. 
Each cell can hold one type of material. To craft a torch, you must place coal above a stick. In total, exactly two 
cells of the four or nine is occupied. It does not matter which ones, as long as the relative positions are maintained. 
Building a bucket, you place iron in a U-pattern in (in total three cells occupied).

Interviewer note: You should draw the matrix with cell content to visualise the problem to the candidate. This question 
also works even though candidate has no idea how Minecraft works. If they are familiar with MC, you might be able to 
skip some bits and pieces when explaining.

Torch: http://minecraft.gamepedia.com/Torch

Bucket: http://minecraft.gamepedia.com/Bucket

See also the old interview document for more examples (pdf)

First part: Craft a torch
Implement data structures and an algorithm that can check for matches of a torch in a 3 x 3 matrix.

Interviewer notes: Candidate is free to choose a data structure they feel that is fit for the task. Usually a 
two-dimensional array or similiar should work.


To check:

Are the data structures extensible for other patterns?
Is the algorithm extensible for other patterns?
What is the complexity of the data structure and algorithm

Second part: Implement the general algorithm
Like above, but implementation of the API for any pattern in any sized matrix.

Solution
One optimal solution is a function that takes the desired pattern and matrix as input. Iterate the matrix one cell at a
time. If a non-empty cell is met, increase counter for non-empty cells and see if the context of that cell is the same 
as the first non-empty item of the pattern. If not, return false. If it matches, do a lookup if other parts of the 
pattern match the cells of the matrix. If not, return false. If they match: iterate to the end and return true iff 
count of empty cells is the same as (matrix size) - (non-empty cells in pattern)

Good pattern alternatives: A two dimensional array, that is a subset of the matrix, a custom class that contains objects
of the pattern described as offset from the first top-left-most non-empty pattern piece. 
"""""

def max_occurance(S):
    if len(S) < 1:
        return None

    elif len(S) == 1:
        return S

    char_count = {}

    # Count the characters
    for char in S:
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1

    # Find the maximum occurance
    max_so_far = None
    has_multiple_maxes = False

    for char in char_count:
        # Because dictionaries are not ordered, we must initialize `max_so_far` inside of the
        # loop.
        if max_so_far is None:
            max_so_far = char
            continue

        # If 2 maximums are equal, then there are no maximums
        if char_count[char] == char_count[max_so_far]:
            has_multiple_maxes = True

        elif char_count[char] > char_count[max_so_far]:
            has_multiple_maxes = False
            max_so_far = char

    return None if has_multiple_maxes else max_so_far


def create_empty_2x2matrix():
    return [[0,0],[0,0]]

def create_empty_3x3matrix():
    return [[0,1,2],[1,0,0],[2,0,0]]

EMPTY = 0
COAL = 1
STICK = 2
IRON = 3

def find_torch(matrix):
    matrix_size = len(matrix)
    row = 0

    for cell in matrix:
        if COAL in cell:
            #found coal make sure cell below is stick
            column = cell.index(COAL)
            if matrix[row+1][column] == STICK:
                return True
        row += 1
        if row == matrix_size-1:
            return False
    return False

def find_item(matrix, item):
    matrix_size = len(matrix)
    item_depth = len(item)
    item_width = len(item[0])
    row = 0
    unique_cell = 0

    # Get first unique block in the item
    for x in range(0, item_width):
        for y in range(0, item_depth):
            if item[y][x]:
                unique_cell = item[y][x]:
                break

    # item was empty, cant match
    if unique_cell == 0:
        return False

    row = 0
    for cell in matrix:
        if unique_cell in cell:
            #found - compare matrix to item at start point...
            column = cell.index(unique_item)
            for x in range(0, item_width):
                for y in range(0, item_depth):
                    if item[y][x]:
            if matrix[row+1][column] == STICK:
                return True
        row += 1
        if row == matrix_size-1:
            return False
    return False

print find_torch([[0,0,COAL],[0,0,STICK],[0,0,0]])
print find_torch([[0,0,COAL],[0,0,0],[0,0,0]])
print find_torch([[0,0,0],[0,0,STICK],[0,0,0]])
print find_torch([[0,0,0],[0,0,STICK],[0,0,COAL]])
print find_torch([[0,0,0],[0,0,COAL],[0,0,STICK]])

mymatrix = [[0,0,0],[0,0,COAL],[0,0,STICK],[0,0,0]]
print len(mymatrix[0]),









