n, m = map(int, input().split(" "))
# v, e
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]



def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

st = []
end = []

for _ in range(m):
    x, y = map(int, input().split(" "))
    st.append(x)
    end.append(y)

for start, end in zip(st, end):
    graph[start].append(end)
    graph[end].append(start)


root_v = 1
cnt = 0
visited[root_v] = True
dfs(root_v)

print(cnt)