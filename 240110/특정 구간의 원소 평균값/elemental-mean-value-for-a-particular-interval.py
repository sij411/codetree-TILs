n = int(input())

arr = list(map(int, input().strip().split(" ")))

cnt = 0

for k in range(1, n): # element nums
    for i in range(n - k + 1):
        tgt = arr[i:i+k]
        mean = sum(tgt)/k
        if mean in tgt:
            cnt += 1

print(cnt)