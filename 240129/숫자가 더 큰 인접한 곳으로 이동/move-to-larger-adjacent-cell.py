n, r, c = map(int, input().strip().split(" "))

grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]



def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate(cur_x, cur_y):

    max_num = grid[cur_x][cur_y]
    max_pos = (-1, -1)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = cur_x + dx, cur_y + dy

        if in_range(next_x, next_y) and \
        grid[next_x][next_y] > max_num:
            max_num = grid[next_x][next_y]
            max_pos = (next_x, next_y)
            break
    cur_x, cur_y = max_pos
    track.append(max_num)
    return cur_x, cur_y

cur_x, cur_y = r - 1, c - 1
# 상 하 좌우 
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

track = [grid[cur_x][cur_y]]

while cur_x >= 0 and cur_y >= 0:
    cur_x, cur_y = simulate(cur_x, cur_y)

for e in range(len(track) - 1):
    print(track[e], end=" ")