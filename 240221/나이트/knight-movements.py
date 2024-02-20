from collections import deque

# 입력
n = int(input())
# start, end
r1, c1, r2, c2 = map(int, input().strip().split(" "))
# grid -> visited only
visited = [[0] * n for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

drs = [-1, -2, -2, -1, 1, 2, 2, 1]
dcs = [-2, -1, 1, 2, 2, 1, -1, -2]

# in range
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    while q:
# 큐 원소 1개 당 이동 가능한 포인트 모두 검사
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc]:
# 가능한 포인트 등장
                visited[nr][nc] = 1
#   방문 처리      
                dist[nr][nc] = dist[r][c] + 1
#   큐에 이동할 점 담기 (그 포인트)
                q.append((nr, nc))
#   이동 횟수 갱신

# variables
q = deque()
visited[r1-1][c1-1] = 1
dist[r1-1][c1-1] = 0
q.append((r1-1, c1-1))
bfs()

print(dist[r2-1][c2-1])