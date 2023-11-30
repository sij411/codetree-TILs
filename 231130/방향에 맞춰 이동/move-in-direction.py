# 0,3
# 2, 3
# 2, 2
# 4, 2

n = int(input()) # how many times

rule = {'W': 0, 'S': 1, 'N': 2, 'E': 3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
x, y = 0, 0

for i in range(n):
    direction, num = input().split()
    num = int(num)

    x = x + (dx[rule[direction]] * num)
    y = y + (dy[rule[direction]] * num)


print(x,y)