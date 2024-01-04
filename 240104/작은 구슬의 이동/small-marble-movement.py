# grid size, t
n, t = map(int, input().strip().split(' '))

# bead info// row, col, current_direction
r, c, cur_dir = input().strip().split(' ')
col = int(r)
row = int(c)

# L U D R
dxs = [0, -1, 1, 0] # row 
dys = [-1, 0, 0, 1]

mapper = {
    'L': 0,
    'U': 1,
    'D': 2,
    'R': 3
}

cur_dir = mapper[cur_dir]

def in_range(x, y):
    return 0 < x and x < n and 0 < y and y < n
# gird

# 구슬 처음 위치 grid[row][col]

# 방향 전환, 시간 1 소요
# !in_range
def change_dir(dir_num):
    return 3 - dir_num
# 이동, 시간 1 소요
def move(dir_num, x, y):
    x += dxs[dir_num]
    y += dys[dir_num]
    return x, y

for _ in range(t):
    if in_range(row, col):
        row, col = row + dxs[cur_dir], col + dys[cur_dir]
        continue
    cur_dir = change_dir(cur_dir)
print(col+1, row+1)