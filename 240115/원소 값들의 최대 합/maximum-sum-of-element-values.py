import copy

n, m = map(int, input().split(" "))
arr = list(map(int, input().strip().split(" ")))

t = 0
for start in range(n):
    d = 0
    idx = start
    for _ in range(m):
        d += arr[idx]
        # print(idx, d)
        if (idx + 1) != arr[idx]:
            idx = arr[idx] - 1   
    t = max(d, t)
    
print(t)