import copy

n, m = map(int, input().split(" "))
arr = list(map(int, input().strip().split(" ")))

def move(start, dest):
    temp = arr[start-1] 
    arr[start-1] = arr[dest-1]
    arr[dest-1] = temp
    return arr

max_cnt = -1
for num in range(1, n+1):
    cnt = 0
    arr_ = copy.deepcopy(arr)
    for _ in range(m):
        start = num
        dest = arr_[start-1]
        cnt += dest
        arr_[start-1] = arr_[dest-1]
        start = arr_[dest-1]
        arr_[dest-1] = dest
    max_cnt = max(cnt, max_cnt)

print(max_cnt)