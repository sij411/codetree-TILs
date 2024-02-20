# grid size, t
n, t = map(int, input().strip().split(' '))

# bead info// row, col, current_direction
# r 행 c 열 i j
x, y, cur_dir = input().strip().split(' ')
x = int(x) - 1
y = int(y) - 1


# L U D R
dys = [-1, 0, 1, 0]  # 열
dxs = [0, -1, 0, 1]  # 행

mapper = {
    'L': 0,
    'U': 1,
    'R': 2,
    'R': 3
}


cur_dir = mapper[cur_dir]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n




for _ in range(t):
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        cur_dir = (cur_dir + 2) % 4


print(x + 1, y + 1)