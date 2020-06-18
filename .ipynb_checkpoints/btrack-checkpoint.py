grid = [[0, 5, 6, 4, 7, 3, 2, 0, 0],
       [0, 2, 9, 0, 0, 0, 7, 8, 0],
       [0, 0, 0, 0, 0, 2, 0, 3, 6],
       [7, 9, 0, 0, 2, 0, 0, 0 ,0],
       [1, 0, 5, 0, 0, 0, 8, 6, 2],
       [6, 0, 0, 8, 3, 0, 0, 7, 1],
       [0, 0, 0, 3, 0, 0, 4, 2, 8], 
       [5, 7, 4, 0, 0, 0, 6, 0, 0],
       [0, 0, 3, 6, 9, 4, 0, 0, 0]]
       
def print_grid():
    for line in grid:
        for square in line:
            if square == 0:
                print(".")
            else:
                print(square)
        print()
        
def possible(y, x, n):
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True
    
    
def solve():
    for y in range(0, 9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return 
    print_grid()
    
if __name__ == '__main__':
    solve()