n, t = map(int, input().split(' '))

grid = [
    list(map(int, input().split()))
    for _ in range(2)
]

def move(grid):
    tmp_up = grid[0][n-1]
    tmp_down = grid[1][n-1]

    for i in range(n-1,0,-1):
        grid[0][i] = grid[0][i-1]
    for j in range(n-1,0,-1):
        grid[1][j] = grid[1][j-1]

    grid[1][0] = tmp_up
    grid[0][0] = tmp_down
    return grid

for _ in range(t):
    grid = move(grid)

for i in range(2):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()