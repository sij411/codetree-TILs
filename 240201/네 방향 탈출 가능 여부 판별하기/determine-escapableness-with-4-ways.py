from collections import deque
n, m = map(int, input().split())
order = 1
# map input
a = [list(map(int, input().split())) for _ in range(n)]
# visited or not
visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs():
    global order
    while q:
        # q를 가지고 너비 우선 탐색
        r, c = q.popleft() # 현재 위치가 r행 c열 탐색 중이다
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc # r, c와 인접한 칸만 (nr, nc) 찾기
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1 and not visited[nr][nc]: # 격자 벗어나지 않는지와 해당 위치에 뱀 없는지 확인, 방문한적 없는지 보고
            # 맞으면 방문한 적 없다는 뜻
            # 방문 순서 표시
                a[nr][nc] = order
                order += 1
                visited[nr][nc] = 1
                q.append((nr, nc))


q = deque()
visited[0][0] = 1
q.append((0, 0))    # 첫번쨰 원소로 0,0 튜플 추가

bfs()
print(visited[n - 1][m - 1])