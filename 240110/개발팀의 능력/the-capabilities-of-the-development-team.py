import math

stats = list(map(int, input().strip().split(" ")))

def get_diff (i, j, team3):
    team1 = stats[i] + stats[j]
    team2 = sum(stats) - team1 - team3
    max_team = max(team1, team2, team3)
    min_team = min(team1, team2, team3)
    if team1 != team2 and team1 != team3 and team2 != team3:
        diff = max_team - min_team
    else:
        diff = -1
    return diff

min_diff = math.inf
for alone in range(5): # 깍듀기
    team3 = stats[alone]
    for i in range(5):
        for j in range(i + 1, 5):
            if i != alone and j != alone and get_diff(i, j, team3) > -1:
                min_diff = min(min_diff, get_diff(i, j, team3))
                # print(f"t1: {stats[i]} {stats[j]} t3: {team3}", min_diff)
if min_diff < math.inf:
    print(min_diff)
else:
    print(-1)