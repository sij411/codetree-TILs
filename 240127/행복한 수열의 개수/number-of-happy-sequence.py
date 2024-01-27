n, m = map(int, input().split(" "))

grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]

# col

hp = 0
for i in range(n):
    max_cnt_col = 0
    cnt = 1
    for j in range(1, n):
        if grid[i][j] == grid[i][j-1]:
            cnt += 1
        else:
            cnt = 1
        max_cnt_col = max(max_cnt_col, cnt)
        # print(max_cnt_col)
    if max_cnt_col >= m:
        hp += 1

# row

for i in range(n):
    max_cnt_row = 0
    cnt = 1
    for j in range(1, n):
        if grid[j][i] == grid[j-1][i]:
            cnt += 1
        else:
            cnt = 1
        max_cnt_row = max(max_cnt_row, cnt)
        # print(max_cnt_row)
    if max_cnt_row >= m:
        hp += 1

print(hp)