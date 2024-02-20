n, m = map(int, input().split(" "))
# 정점과 간선
graph = [[] for _ in range(n + 1)]

# 정점 방문 여부
visited = [False for _ in range(n + 1)]



def dfs(vertex):
    global cnt
    # 해당 정점에서 연결되어 있는 모든 정점 탐색
    for curr_v in graph[vertex]:
        # 간선 존재 && 방문한 적이 없는 정점에 대해서만 탐색 진행
        if not visited[curr_v]:
            # 방문 횟수 증가
            cnt += 1
            visited[curr_v] = True
            # 마지막으로 방문한 정점에 연결된 정점을 탐색하므로 재귀 호출
            dfs(curr_v)

for i in range(m):
    x, y = map(int, input().split(" "))
    # 양방향 그래프이기 때문에 각 정점에 대한 간선을 각각 저장해줍니다.
    graph[x].append(y)
    graph[y].append(x)


cnt = 0
visited[1] = True
dfs(1)

print(cnt)