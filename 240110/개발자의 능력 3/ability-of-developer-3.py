import math

stats = list(map(int, input().strip().split(" ")))

def get_diff(i, j, k):
    team1 = stats[i] + stats[j] + stats[k]
    team2 = sum(stats) - team1
    return abs(team1 - team2)

n = len(stats)
min_diff = math.inf
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            min_diff = min(min_diff, get_diff(i,j,k))


print(min_diff)