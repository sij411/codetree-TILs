n, k = map(int, input().split(" "))

pos = [0 for _ in range(10000)]
for i in range(n):
    p, alphabet = input().split(" ")
    if alphabet == 'G':
        pos[int(p)-1] = 1
    elif alphabet == 'H':
        pos[int(p)-1] = 2


max_cnt = 0
cnt = 0
for j in range(len(pos)-k+1):
    cnt = sum(pos[j:j+k])
    max_cnt = max(max_cnt, cnt)
   
print(max_cnt)