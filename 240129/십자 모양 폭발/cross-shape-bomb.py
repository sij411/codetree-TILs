n = int(input())

# grid

grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]

r, c = map(int, input().split(" "))

# print(grid)
# print(x, y) # -1해줘야 함

r, c = r - 1, c - 1

for k in range(grid[r][c]):
    grid[r + k][c] = 0
    grid[r - k][c] = 0
    grid[r][c + k] = 0
    grid[r][c - k] = 0

# 폭탄 터진 후 확인
print(grid)

temp = [[0] * n for _ in range(n)]

print(temp_row)
for col in range(n):
    temp_row = n - 1
    for row in range(n - 1, -1, -1):
        temp[3][col] = grid[row][col] # gravity -> 맨 밑부터 쌓여야 함
        temp_row -= 1
       
print(temp)