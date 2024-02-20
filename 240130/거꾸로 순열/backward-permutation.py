n = int(input())
visited = [False] * (n + 1)
ans = []

def print_answer():
    for elem in ans:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = True
        ans.append(i)

        choose(curr_num + 1)

        ans.pop()
        visited[i] = False

choose(1)