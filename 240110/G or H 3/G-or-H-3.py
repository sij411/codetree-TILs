n, k = map(int, input().split(" "))

pos = [0 for _ in range(10000)]
m = 0
l = 0
for i in range(n):
    p, alphabet = input().split(" ")
    if alphabet == 'G':
        pos[int(p)] = 1
    elif alphabet == 'H':
        pos[int(p)] = 2
    if m < int(p):
        m = int(p)
    if l > int(p):
        l = int(p)
# print(m)

max_cnt = 0
cnt = 0
for j in range(10000-k+1):
 
    cnt = sum(pos[j:j+k+1])
    max_cnt = max(max_cnt, cnt)
   
print(max_cnt)