n, c, g, f = map(int, input().strip().split(" "))

def get_workload(cur_t, ta, tb):
    if cur_t < ta:
        return c
    elif ta <= cur_t <= tb:
        return g
    elif cur_t > tb:
        return f
    else:
        return 0

max_total = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split(" "))))

for t in range(1001):
    cur_workload = 0
    for i in range(n):
        ta, tb = arr[i][0], arr[i][1]
        cur_workload += get_workload(t, ta, tb)
    max_total = max(max_total, cur_workload)

print(max_total)