n, m = map(int, input().split(" "))

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n + 1)]

# init
for _ in range(m):
    x, y = map(int, input().split(" "))
    # 양방향 그래프이기 때문에 각 정점에 대한 간선을 각각 저장해줍니다.
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    global cnt
    for curr_v in graph[v]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

cnt = 0
visited[1] = True
dfs(1)

print(cnt)