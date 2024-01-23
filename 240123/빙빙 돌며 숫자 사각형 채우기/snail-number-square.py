n, m = map(int, input().strip().split(" "))

grid = [[0 for y in range(m)] for x in range(n)]

# 오른쪽, 아래, 왼, 위
# +2 반대
dy = [1,0,-1,0]
dx = [0,1,0,-1]
dir_num = 0 # right (default)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

num = 1
x, y = 0, 0
grid[x][y] = num

for _ in range(n*m-1):
    num += 1
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if in_range(nx, ny) and grid[nx][ny] == 0:
        x, y = nx, ny 
    else:
        dir_num = (dir_num + 1) % 4
        x, y = x + dx[dir_num], y + dy[dir_num]
    grid[x][y] = num

   
        

for x in range(0, n):
    for y in range(0, m):
        print(grid[x][y], end=' ')
    print()