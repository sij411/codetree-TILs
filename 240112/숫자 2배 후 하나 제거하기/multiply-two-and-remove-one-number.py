import sys

n = int(input())

arr = list(map(int, input().strip().split(' ')))
min_cnt = sys.maxsize

for i in range(n):
    arr_ = [elem for k, elem in enumerate(arr)]
    arr_[i] = arr_[i] * 2
    for j in range(n):
        arr_removed = [elem for k, elem in enumerate(arr_) if k !=j]
        cnt = 0
        for l in range(len(arr_removed)-1):
            cnt += abs(arr_removed[l] - arr_removed[l+1])
        min_cnt = min(cnt, min_cnt)
        

print(min_cnt)