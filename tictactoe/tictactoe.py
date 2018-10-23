import random

NUM_ROWS = 3
NUM_COLUMNS = 3
PLAYER_COLOUR = '\033[93m'
COMPUTER_COLOUR = '\033[91m'
END_COLOUR = '\033[0m'
num_rounds = 0

def get_player_name():
    name = raw_input("What is your name? ")
    #name = "John"
    print(PLAYER_COLOUR + "Welcome {}".format(name) + END_COLOUR)
    return name

def init():
    # TODO list comprehension
    grid = []
    for i in range(0, NUM_ROWS):
        grid.append([])
        for j in range(0, NUM_COLUMNS):
            grid[i].append(0)
            
    return grid
    
def print_grid(grid):
    print("")
    print "\t      1   2   3"
    print("")
    for i in range(0, len(grid)):
        print "\t {}  |".format(str(i + 1)),
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                print PLAYER_COLOUR + "x" + END_COLOUR,
            elif grid[i][j] == 2:
                print COMPUTER_COLOUR + "o" + END_COLOUR,
            else:
                print " ",
            
            print "|",
            
        print ""
        if i < len(grid) - 1:
            print "\t   ",
            print("-" * 13)
    
    print ""
    
def parse_coordinates(coordinates):
    row = coordinates[0]
    column = coordinates[1]
    return row, column
    
def prompt_player(name):
    are_coordinates_valid = False
    while not are_coordinates_valid:
        coordinates = raw_input("It's your turn {}: ".format(name))
        row, column = parse_coordinates(coordinates)
        if column.isdigit() and int(column) > 0 and int(column) <= NUM_COLUMNS and row.isdigit() and int(row) > 0 and int(row) <= NUM_ROWS:
            are_coordinates_valid = True
        else:
            print("You must enter coordinates in the format rowcolumn, like 12 (first row, second column). Try again.")
            
    return int(row) - 1, int(column) - 1
    
def is_position_taken(row, column, grid):
    return grid[row][column] > 0
    
def update_grid(grid, row, column, player):
    grid[row][column] = player
    
def computer_plays(grid):
    print("Computer's turn...")
    position_taken = True
    while position_taken:
        row, column = prompt_computer()
        position_taken = is_position_taken(row, column, grid)
        
    print("Playing on row {} and column {}".format(row + 1, column + 1))
    
    return row, column
    
def player_plays(name, grid):
    position_taken = True
    while position_taken:
        row, column = prompt_player(name)
        position_taken = is_position_taken(row, column, grid)
        if position_taken:
            print("Positon ({}, {}) is already taken. Try again.".format(row + 1, column + 1))
            
    return row, column

def prompt_computer():
    row = random.randint(0, NUM_ROWS - 1)
    column = random.randint(0, NUM_COLUMNS - 1)
    
    return row, column
    
def play():
    name = get_player_name()
    grid = init()
    row, column = -1, -1
    winner = 0
    num_rounds = 0
    total_rounds = NUM_ROWS * NUM_COLUMNS
    while num_rounds < total_rounds:
        print_grid(grid)
        row, column = player_plays(name, grid)        
        update_grid(grid, row, column, 1)
        print_grid(grid)
        
        # TODO check winner
        
        num_rounds += 1
        
        row, column = computer_plays(grid)
        update_grid(grid, row, column, 2)
    
play()