n, K = map(int, input().split(" "))
elements = []
for _ in range(n):
    elements.append(int(input()))

elements.sort()
max_cnt = 0
max_elem = max(elements)
min_elem = min(elements)
diff = max_elem - min_elem
for k in range(K+1):
    if k > diff:
        continue
    for i in range(n):
        for j in range(i+1, n):
            cnt = 0
            if abs(elements[i] - elements[j]) == k:
                # print(elements[i], elements[j])
                cnt += len(elements[i:j+1])
                max_cnt = max(cnt, max_cnt)
                # print(k,i,j, max_cnt)
                

print(max_cnt)