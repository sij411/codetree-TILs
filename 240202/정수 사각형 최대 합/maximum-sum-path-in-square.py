import sys

MIN_INT = -sys.maxsize

# 입력
n = int(input())
grid = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

DP = [
    [MIN_INT] * n
    for _ in range(n)
]

# 디피 테이블 초기화
def initialize():
    DP[0][0] = grid[0][0]
    DP[0][1] = grid[0][1]
    DP[0][2] = grid[0][2]

    for i in range(1, n):
    # 첫 번째 열에 대한 초깃값
        DP[i][0] = DP[i - 1][0] + grid[i][0]

        DP[i][i] = DP[i - 1][i - 1] + grid[i][i]


initialize()



for i in range(1, n):
    for j in range(1, n):
        DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) + grid[i][j]

print(DP[n-1][n-1])