n, k = map(int, input().split(' '))

arr = list(map(int, input().strip().split(" ")))


result = 0
for i in range(n-k+1):
    cnt = 0
    for j in range(i, i+k):
        cnt += arr[j]
    result = max(result, cnt)

print(result)