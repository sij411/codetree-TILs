# 입력
n, m = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = [0 for _ in range(n+1)]
for _ in range(m):
    v, e = map(int, input().split(" "))
    graph[v].append(e)
    graph[e].append(v)
# 가장 많은 정점으로 갈 수 있다 -> 연결된 정점이 젤 많다?

def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)


max_cnt = 0
ans = 1
for v in range(n+1):
    visited[v] = True
    cnt = 0
    dfs(v)
    if cnt > max_cnt:
        max_cnt = cnt
        ans = v

for v in graph[v]:
    print(v, end=" ")