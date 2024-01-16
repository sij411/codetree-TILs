n, k = map(int, input().split(" "))
elements = []
for _ in range(n):
    elements.append(int(input()))

elements = sorted(elements)
max_cnt = 0
max_elem = max(elements)
min_elem = min(elements)
diff = max_elem - min_elem

i, j = 0, 1
while j < n :
    if elements[j] - elements[i] == k and i != j:
        cnt = j - i + 1 # idx 차이 == 개수 이미 정렬했으므로 해당 인덱스 범위 내에 있는 숫자들은 구간 안에 있음. 
        max_cnt = max(cnt, max_cnt)
            # print(f"k: {k}, i: {i}, j: {j}, cnt: {cnt}") 
        j += 1
    elif elements[j] - elements[i] > k:
        i += 1
    else:
        j += 1
    
    
                

print(max_cnt)