n = int(input())

# grid

grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]

r, c = map(int, input().split(" "))

# print(grid)
# print(x, y) # -1해줘야 함

r, c = r - 1, c - 1

for k in range(grid[r][c]):
    if r + k < n:
        grid[r + k][c] = 0
    if r - k >= 0:
        grid[r - k][c] = 0
    if c + k < n:
        grid[r][c + k] = 0
    if c - k >= 0:
        grid[r][c - k] = 0


temp = [[0] * n for _ in range(n)]


for col in range(n):
    temp_row = n - 1
    for row in range(n - 1, -1, -1):
        if grid[row][col] != 0:
            temp[temp_row][col] = grid[row][col] # gravity -> 맨 밑부터 쌓여야 함
            temp_row -= 1
        
for i in range(n):
    for j in range(n):
        grid[i][j] = temp[i][j]
        print(grid[i][j], end=" ")
    print()