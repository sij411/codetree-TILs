n, k = map(int, input().split(" "))

pos = [0 for _ in range(10000)]
for i in range(n):
    p, alphabet = input().split(" ")
    pos[int(p)-1] = alphabet
# print(pos[:20])

max_cnt = 0
for i in range(n-k+1):
    cnt = 0
    for j in range(i, i+k+1):
        if pos[j] == 'G':
            cnt += 1
        elif pos[j] == 'H':
            cnt += 2
    max_cnt = max(max_cnt, cnt)


print(max_cnt)