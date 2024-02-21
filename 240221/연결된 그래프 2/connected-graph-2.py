# 입력
n, m = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]

count = [0 for _ in range(n+1)]
for _ in range(m):
    v, e = map(int, input().split(" "))
    graph[v].append(e)
    
# 가장 많은 정점으로 갈 수 있다 -> 연결된 정점이 젤 많다?

def dfs(vertex):
    
    for curr_v in graph[vertex]:
     
        count[curr_v] += 1
     


for v in range(1, n+1):
    dfs(v)



ans = count.index(max(count))
for i in range(1, n+1):
    for e in graph[i]:
        # print(i, e, ans)
        if e == ans:
            print(i, end=" ")