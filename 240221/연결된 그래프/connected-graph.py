def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 입력 받기
n, m = map(int, input().split())
graph = {i: set() for i in range(1, n+1)}

# 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)  # 무방향 그래프이므로 양쪽에 추가

# DFS 실행
visited = set()
dfs(graph, 1, visited)

# 출력: 1번 노드를 제외한 연결된 노드의 개수
print(len(visited) - 1)