# 격자 행
n = int(input())
# 격자
grid = []


for _ in range(n):
    arr = list(map(int, input().strip().split(' ')))
    grid.append(arr)
    
    
# print(grid)
# 상하좌우 
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]
# in_range
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
# 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수 세기 (inRange and )

total_cnt = 0
for i in range(n):
    x = i
    for j in range(n):
        y = j
        count = 0
        for dx, dy in zip(dxs, dys):
            cur_x, cur_y = x + dx, y + dy
            if in_range(cur_x, cur_y) and grid[cur_x][cur_y] == 1:
                count += 1
        if count >= 3:
            total_cnt += 1

print(total_cnt)