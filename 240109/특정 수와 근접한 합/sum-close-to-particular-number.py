import sys

n, s = map(int, input().split(" "))

arr = list(map(int, input().split(" ")))

MAX = sys.maxsize
result = MAX
x = 0
y = 0
for i in range(n):
    cnt = 0 
    for j in range(n):
        if j != i:
            num = arr.copy()
            num[i] = 0
            num[j] = 0
            cnt = sum(num)
            if result > abs(cnt - s):
                result = cnt - s
                


print(result)