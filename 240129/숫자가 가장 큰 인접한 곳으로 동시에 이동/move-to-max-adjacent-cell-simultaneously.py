n, m, t = map(int, input().strip().split(" "))

grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]

beads = [tuple(map(int, input().split(" "))) for _ in range(m)] # -1 

# count init
count = [[0] * n for _ in range(n)]

for x, y in beads:
    count[x - 1][y - 1] += 1

# next count arr ready
next_count = [[0] * n for _ in range(n)]

# dxs dys
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# in range
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# get next pos
def get_next_pos(cur_x, cur_y):

    max_num = 0
    max_pos = (cur_x, cur_y)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = cur_x + dx, cur_y + dy

        if in_range(next_x, next_y) and \
        grid[next_x][next_y] > max_num:
            max_num = grid[next_x][next_y]
            max_pos = (next_x, next_y)

    cur_x, cur_y = max_pos
    return cur_x, cur_y
# move bead 
def move(x, y):
    next_x, next_y = get_next_pos(x, y)

    next_count[next_x][next_y] += 1

def move_all():
    # next_count init
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0

    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

def remove_collision():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0


def simulate():
    move_all()
    remove_collision()


for _ in range(t):
    simulate()

cnt = 0
for i in range(n):
    cnt += sum(count[i])

print(cnt)