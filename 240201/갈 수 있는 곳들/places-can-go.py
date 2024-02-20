from collections import deque

# n은 격자 크기, 후자는 시작점의 수
n, k = map(int, input().split())
order = 1

# map input
a = [list(map(int, input().split())) for _ in range(n)]

# 시작 정점
vertexes = [tuple(map(int, input().split(" "))) for _ in range(k)]

def bfs():
    # global order
    global cnt
    while q:
        # q를 가지고 너비 우선 탐색
        r, c = q.popleft() # 현재 위치가 r행 c열 탐색 중이다
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc # r, c와 인접한 칸만 (nr, nc) 찾기
            if 0 <= nr < n and 0 <= nc < n and a[nr][nc] == 0 and not visited[nr][nc]: # 격자 벗어나지 않는지와 해당 위치에 뱀 없는지 확인, 방문한적 없는지 보고
            # 맞으면 방문한 적 없다는 뜻
            # 방문 순서 표시
                # a[nr][nc] = order
                # order += 1
                cnt += 1
                visited[nr][nc] = 1
                q.append((nr, nc))

visited = [[0] * n for _ in range(n)]

cnt = 0

for x, y in vertexes:
# visited or not
    q = deque()
    if not visited[x - 1][y - 1]:
        visited[x - 1][y - 1] = 1
        cnt += 1
        q.append((x - 1, y - 1))    # 첫번쨰 원소로 0,0 튜플 추가
        bfs()

print(cnt)