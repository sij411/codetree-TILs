import math

n, h, t = map(int, input().strip().split(" "))

field = list(map(int, input().strip().split(" ")))

min_cost = math.inf

for i in range(t, n+1): # range
    for j in range(n-i+1):
        cost = 0
        for k in range(j, j+i):
            # print(f"range{i} start{k} ")
            cost += abs(h-field[k])
        if min_cost > cost:
            min_cost = cost

print(min_cost)