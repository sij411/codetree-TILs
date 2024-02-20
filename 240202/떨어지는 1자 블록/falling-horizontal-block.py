# 격자 크기, 블록 크기, 블록이 떨어질 위치
n, m, k = tuple(map(int, input().strip().split(" ")))

grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]


# 해당 로우에 [col_s, col_e] 열에 전부 블럭이 없는지 확인한다
def all_blank(row, col_s, col_e):
    return all([
        not grid[row][col]
        for col in range(col_s, col_e + 1)
    ])

# 최종적으로 도달할 위치는 그 다음 위치에 최초로 블럭이 존재하는 순간임을 이용.
# 바로 다음 줄이 블럭이 있는 곳
def get_target_row():
    for row in range(n - 1):
        if not all_blank(row + 1, k, k + m - 1):
            return row
    return n - 1

k -= 1

target_now = get_target_row()

for col in range(k, k + m):
    grid[target_now][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()