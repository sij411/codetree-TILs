n, c, g, h = map(int, input().strip().split(" "))

def get_workload(cur_t, ta, tb):
    if cur_t < ta:
        return c
    elif cur_t <= tb:
        return g
    else:
        return h

max_total = 0
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split(" "))))

for t in range(1001):
    cur_workload = 0
    for i in range(n):
        cur_workload += get_workload(t, arr[i][0], arr[i][1])
    max_total = max(max_total, cur_workload)

print(max_total)