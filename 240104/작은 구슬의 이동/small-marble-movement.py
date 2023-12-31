# grid size, t
n, t = map(int, input().strip().split(' '))

# bead info// row, col, current_direction
# r 행 c 열 i j
x, y, cur_dir = input().strip().split(' ')
x = int(x) - 1
y = int(y) - 1


# L U D R
dys = [-1, 0, 0, 1]  # 열
dxs = [0, -1, 1, 0]  # 행

mapper = {
    'L': 0,
    'U': 1,
    'D': 2,
    'R': 3
}

cur_dir = mapper[cur_dir]


def can_not_move_side(x, dir_num):
    return (x <= 0 and dir_num == 0) or (x >= n - 1 and dir_num == 3)


def can_not_move_upside(y, dir_num):
    return (y <= 0 and dir_num == 1) or (y >= n - 1 and dir_num == 2)


# gird

# 구슬 처음 위치 grid[row][col]

# 방향 전환, 시간 1 소요
# !in_range
def change_dir(dir_num):
    return 3 - dir_num


cur_t = 0
while cur_t < t:
    if cur_dir in [0, 3] and can_not_move_side(y, cur_dir):
        cur_dir = change_dir(cur_dir)
        cur_t += 1
        continue
    elif cur_dir in [1, 2] and can_not_move_upside(x, cur_dir):
        cur_dir = change_dir(cur_dir)
        cur_t += 1
        continue
    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    cur_t += 1

print(x + 1, y + 1)