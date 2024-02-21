from collections import deque
# 입력 : 격자 크기, 시작점 개수, 치울 돌 개수, 격자 , 시작점 위치 
n, k, m = map(int, input().strip().split(" "))
grid = [list(map(int, input().split())) for _ in range(n)]
start = []
for _ in range(k):
    start.append(tuple(map(int, input().split(" "))))
# 미리 돌이 어디있는지 알아놓으면 좋지 않을까?
stone = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1:
            stone.append((x, y))

# 상하좌우 인접 칸 중 0인 곳으로 이동한다. 
# 이동할 때마다 이동 횟수를 카운트
def bfs(q, cnt, grid, visited):
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and not visited[nr][nc]:
                cnt += 1
                visited[nr][nc] = 1
                q.append((nr, nc))
    return cnt

# 작업
# m개의 돌을 치운다.


def choose_stone(grid, curr_cnt):
    global max_cnt
    # 돌 m개째 치우면 종료
    if curr_cnt == m:
        for r, c in start:
            q = deque()
            visited = [[0] * n for _ in range(n)]
            visited[r-1][c-1] = 1
            q.append((r-1, c-1))
            cnt = bfs(q, 1, grid, visited)
            max_cnt = max(max_cnt, cnt)
        return 
    
    for st in stone:
        x, y = st[0], st[1]
        if grid[x][y] == 0:
            continue
        # 돌자 치워
        grid[x][y] = 0
        # 돌자1 치운 상태에서 다른 돌자 치워
        choose_stone(grid, curr_cnt + 1)
        # 돌자 원상복귀
        grid[x][y] = 1



# 달라지는 조건
# 돌의 위치
# 시작점 만큼 돌자 치우기 반복

# 전체 돌 치우기는 시작점 개수 * mC전체돌개수

# 시작점 1개에 대한 위치별 돌 치우기 작업


   

max_cnt = 0

choose_stone(grid, 0)
print(max_cnt)