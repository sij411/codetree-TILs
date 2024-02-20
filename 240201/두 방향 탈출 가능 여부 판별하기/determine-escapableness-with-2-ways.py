# input 
# grid size n * m
n, m = map(int, input().split(" "))

# repeat n times 
grid = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

visited = [[0] * m for _ in range(n)]

order = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    # 방문 순서를 표시하기 위한 변수
    global order

    # 아래와 오른쪽 이동을 위함
    dxs, dys = [1, 0], [0, 1]
    
    # 방문 순서 표시
    grid[x][y] = order
    # 방문 순서 증가
    order += 1
    # 정점 방문 여부 갱신
    visited[x][y] = 1

    # 아래나 오른쪽 중 가능한 곳으로 먼저 이동하기
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)

dfs(0, 0)

print(visited[n - 1][m - 1])