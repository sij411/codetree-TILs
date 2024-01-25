n = int(input())

grid = []
for _ in range(n):
    _arr = list(map(int, input().strip().split(" ")))
    grid.append(_arr)



# 어떻게  3 3 격자 안을 설정?

    # 가로는 0, 1, 2, ... n-3
    # 세로는 0, 1, 2, ... n-3
    # 가로 인덱스 0이면 grid[0][:3] + grid[1][:3] + grid[2][:3]
    # idx : 1 grid[0][1:1+3] + grid[1][1:1+3] + grid[2][1:1+3]


max_coins = 0
ans = [[], [], []]
for j in range(n-3+1):
    for i in range(n-3+1):
        coin = sum(grid[j][i:i+3] + grid[j+1][i:i+3] + grid[j+2][i:i+3])
        if max_coins < coin:
            max_coins = coin
            ans[0] = grid[j][i:i+3]
            ans[1] = grid[j+1][i:i+3]
            ans[2] = grid[j+2][i:i+3]

print(max_coins)