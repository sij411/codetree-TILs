n, K = map(int, input().split(" "))
elements = []
for _ in range(n):
    elements.append(int(input()))

elements.sort()
max_cnt = 0

for k in range(K+1):
    for i in range(n):
        for j in range(i+1, n):
            cnt = 0
            if abs(elements[i] - elements[j]) == k:
                # print(elements[i], elements[j])
                cnt += len(elements[i:j+1])
                max_cnt = max(cnt, max_cnt)
                # print(k,i,j, max_cnt)
                

print(max_cnt)