# 알바 

# 입력 : 알바 정보의 개수, 알바 정보 
n = int(input())
part_time = [tuple(map(int, input().strip().split(" "))) for _ in range(n)]
dp = [0] * n

# 1개만 하기 
for i in range(n):
    dp[i] = part_time[i][2]

# 2개 (종료일과 시작일이 달라야 함.)

# dp : i번째 사람이 받을 수 있는 최대값
# 시작일 이전에 존재하는 것만?

# 알바를 통해 얻을 수 있는 최대 금액
# 일정이 맞으면서 가장 최대인 거 2개.
# n * n 행렬

# dp definition : max part time pay? 
# dp[i] = grid[i], grid[j] + dp[i]

# 2개 하기
for i in range(n):
    for j in range(i):
        if part_time[j][1] < part_time[i][0]:
            # 하나만 하기 or 이번 알바비 + before
            dp[i] = max(dp[i], part_time[i][2] + dp[j])

ans = dp[0]
for i in range(n):
    ans = max(ans, dp[i])

print(ans)