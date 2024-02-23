# 입력 : 행렬 크기, 행렬
n = int(input())
grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
# 이동 : 오른쪽, 밑 (0, -1) (1, 0)

# 매번 이동 시 검사하는 것 : 이동했을 때 거쳐간 위치에 적혀있는 숫자들 중 최댓값 찾기 (경로별 )
# 테이블 갱신 값 : 오른쪽으로 이동 아니면 아래로 이동했을 때 검사한 각 최댓값 중 최솟값 (두 가지 경로에서 최소)

# 항상 최솟값으로 테이블을 채우자

# 경로가 2개 이상인 칸부터 최솟값

# 디피 테이블은 한 가지 경로에 대해서 경로를 종류별로 두 번 계산하고 최솟값
# 본인 숫자는 제외?
# (1,1) 까지 올 수 있는 경로는?
# 1 4 (1,1) 이 중 최댓값은 4
# 1, 3 (1,1) 최댓값은 3 최소는 3?
# 테이블 왼쪽, 위쪽 중 작은 거 대 해당 칸 (셋 중에서 젤 작은거?)
# 최대
# 1 4 4
# 3 4 5
# 5 (5, 4) (5, 4)


for j in range(n):
    if j == 0:
        dp[0][0] = grid[0][0]
    else:
        dp[0][j] = max(dp[0][j-1], grid[0][j])

for i in range(n):
    if i == 0:
        dp[0][0] = grid[0][0]
    else:
        dp[i][0] = max(dp[i-1][0], grid[0][j])

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i][j-1], dp[i-1][j]), grid[i][j])

print(dp[n-1][n-1])