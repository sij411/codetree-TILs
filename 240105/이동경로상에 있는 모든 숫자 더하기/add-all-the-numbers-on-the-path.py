# grid: n by n
# start: middle of the grid

# L: 270 deg (-90 deg)
# R: 90 deg
# F: front (1 block)

# Add the number on the block
# Ignore the command which makes the ball out of the grid

'''
    input: N(grid), T(the number of commands), command, 

'''

n, t = map(int, input().split(' '))

command = input()

# grid
grid = []
for i in range(n):
    arr =input().strip().split(' ')
    arr_int = [int(i) for i in arr]
    grid.append(arr_int)

# middle
m = n//2

# x == row, y == col
# north east south west
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def turn_left(d):
    return (d -1 + 4) % 4

def turn_right(d):
    return (d + 1) % 3

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
total = 0
num = grid[m][m]
cur_x, cur_y = m, m
total += num
d = 0

for i in range(t):
    if command[i] == 'R':
        d = turn_right(d)
    elif command[i] == 'L':
        d = turn_left(d)
    else:
        temp_x, temp_y = cur_x + dxs[d], cur_y + dys[d]
        if in_range(temp_x, temp_y):
            cur_x = temp_x
            cur_y = temp_y
            num = grid[cur_x][cur_y]
            total += num
            # print("current", cur_x, cur_y, total)

# x, y = x + dxs[d], y + dys[d]


print(total)