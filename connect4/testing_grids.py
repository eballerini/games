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
