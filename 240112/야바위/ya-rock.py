n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split(" "))))

# a = 1
# exchange 1 2 1 -> 0 1 0
max_ = -1
for stone in range(3):
    cnt = 0
    record = [0] * 3
    record[stone] = 1
    for game in arr:
        ex1 = game[0] - 1 # 0
        ex2 = game[1] - 1 # 1
        
        temp = record[ex1]
        record[ex1] = record[ex2]
        record[ex2] = temp 
        target = record[game[2] - 1]
        
        cnt += target
    max_ = max(max_, cnt)


print(max_)