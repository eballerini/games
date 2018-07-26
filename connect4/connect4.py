import random

NUM_ROWS = 6
NUM_COLUMNS = 7
PLAYER_COLOUR = '\033[93m'
COMPUTER_COLOUR = '\033[91m'
END_COLOUR = '\033[0m'
num_rounds = 0

def get_player_name():
    #name = raw_input("What is your name? ")
    name = "John"
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
    
def load_vertical_grid_1(grid):
    grid[0][0] = 1
    grid[1][0] = 1
    grid[2][0] = 1
    #grid[3][0] = 1
    #grid[4][0] = 1
    #grid[5][0] = 1
    grid[0][4] = 2
    
def load_vertical_grid_2(grid):
    grid[0][0] = 2
    grid[1][0] = 2
    grid[2][0] = 1
    grid[3][0] = 1
    grid[4][0] = 1
    #grid[5][0] = 1
    grid[0][4] = 2
    
def load_horizontal_grid_1(grid):
    grid[0][0] = 1
    grid[0][1] = 1
    grid[0][2] = 2
    grid[0][3] = 1
    grid[0][4] = 1
    grid[0][5] = 1
    grid[1][2] = 1
    grid[1][3] = 1
    grid[1][4] = 1
    
def load_horizontal_grid_2(grid):
    grid[0][2] = 2
    grid[0][3] = 2
    grid[0][4] = 2
    
def load_diagonal_grid_1(grid):
    #grid[0][0] = 1
    
    #grid[0][1] = 1
    #grid[1][1] = 1
    
    grid[1][2] = 2
    grid[0][2] = 2
    grid[2][2] = 1
    grid[0][3] = 1
    grid[0][4] = 1
    grid[0][5] = 2
    
    grid[1][3] = 1
    grid[1][3] = 1
    grid[1][4] = 2
    
    grid[2][3] = 2
    grid[3][3] = 1
    
    grid[2][4] = 1
    grid[3][4] = 2
    
def horizontal_check(grid):
    for i in range(0, NUM_ROWS):
        num_disks = 0
        player = grid[i][0]
        if player != 0:
            num_disks = 1
        for j in range(1, NUM_COLUMNS):
            if grid[i][j] == player and player != 0:
                num_disks += 1
            else:
                player = grid[i][j]
                if player != 0:
                    num_disks = 1
                else:
                    num_disks = 0
            if num_disks >= 4:
                return player
    return 0
    
def vertical_check(grid):
    for j in range(0, NUM_COLUMNS):
        num_disks = 0
        player = grid[0][j]
        if player != 0:
            num_disks = 1
        for i in range(1, NUM_ROWS):
            if grid[i][j] == player and player != 0:
                num_disks += 1
            else:
                player = grid[i][j]
                if player != 0:
                    num_disks = 1
                else:
                    num_disks = 0
            if num_disks >= 4:
                return player
    return 0

def diagonal_check(grid):
    up_and_left = diagonal_check_up_and_left(grid)
    if up_and_left > 0:
        return up_and_left
        
    return diagonal_check_up_and_right(grid)
        
def diagonal_check_up_and_right(grid):
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            player = grid[i][j]
            if player != 0:
                num_disks = 1
                current_row = i
                current_col = j
                check_diagonal = True
                while current_row + 1 < NUM_ROWS and current_col + 1 < NUM_COLUMNS and check_diagonal:
                    current_row += 1                
                    current_col += 1
                    if grid[current_row][current_col] == player:
                        num_disks += 1
                        if num_disks >= 4:
                            return player
                    else:
                        check_diagonal = False
            else:
                continue
                
    return 0
    
def diagonal_check_up_and_left(grid):
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            player = grid[i][j]
            if player != 0:
                num_disks = 1
                current_row = i
                current_col = j
                check_diagonal = True
                while current_row + 1 < NUM_ROWS and current_col - 1 > 0 and check_diagonal:
                    current_row += 1                
                    current_col -= 1
                    if grid[current_row][current_col] == player:
                        num_disks += 1
                        if num_disks >= 4:
                            return player
                    else:
                        check_diagonal = False
            else:
                continue
                
    return 0
                        
    
def game_over(grid):
    horizontal_win_player = horizontal_check(grid)
    if horizontal_win_player > 0:
        return horizontal_win_player
            
    vertical_win_player = vertical_check(grid)
    if vertical_win_player > 0:
        return vertical_win_player
        
    diagonal_win_player = diagonal_check(grid)
    if diagonal_win_player > 0:
        return diagonal_win_player
    
    return 0
    
def print_grid(grid):
    print("")
    for i in range(len(grid) - 1, -1, -1):
        print "\t|",
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                print PLAYER_COLOUR + "x" + END_COLOUR,
            elif grid[i][j] == 2:
                print COMPUTER_COLOUR + "o" + END_COLOUR,
            else:
                print " ",
            
            print "|",
            
        print ""
    
    print "\t",
    print("_" * 29)
    print ""
        
        
def player_plays(name):
    is_column_valid = False
    while not is_column_valid:
        column = raw_input("It's your turn {}: ".format(name))
        if column.isdigit() and int(column) > 0 and int(column) <= NUM_COLUMNS:
            is_column_valid = True
        else:
            print("You must enter a column between 1 and {}. Try again.".format(NUM_COLUMNS))
            
    return int(column) - 1
    
def is_column_full(column, grid):
    return grid[NUM_ROWS - 1][column] != 0

def update_grid(grid, column, player):
    row = 0
    while grid[row][column] != 0:
        row += 1
    grid[row][column] = player
    
def computer_plays():
    return random.randint(0, NUM_COLUMNS - 1)
    
name = get_player_name()
grid = init()
#load_horizontal_grid_2(grid)
column = 0
winner = 0
num_rounds = 0
total_rounds = NUM_ROWS * NUM_COLUMNS
while num_rounds < total_rounds:
    print_grid(grid)
    column_full = True
    while column_full:
        column = player_plays(name)
        column_full = is_column_full(column, grid)
        if column_full:
            print("Column {} is full. Try again.".format(column + 1))
        
    update_grid(grid, column, 1)
    winner = game_over(grid)
    if winner > 0:
        break
        
    num_rounds += 1
    
    print("Computer's turn...")
    column_full = True
    while column_full:
        column = computer_plays()
        print("Trying column {}...".format(column + 1))
        column_full = is_column_full(column, grid)
        
    print("Playing on column {}".format(column + 1))
    update_grid(grid, column, 2)
    
    num_rounds += 1
    
    winner = game_over(grid)
    if winner > 0:
        break

print_grid(grid)

if winner > 0:
    if winner == 1:
        winner_name = name
    else: 
        winner_name = "Computer"
    print("Game is over. {} wins".format(winner_name))
else:
    print("Game is over. It a tie")
# if winner == 1:
#     winner_name = name
# else:
#     winner_name = "Computer"
    
