import sys

n = int(input()) # the num of dots

cord = []
for _ in range(n):
    arr = list(map(int, input().split(' ')))
    cord.append(arr)

for i in range(n): # 제외시킬 좌표의 인덱스
    min_square = sys.maxsize
    for j in range(n):
        max_x, max_y, min_x, min_y = -sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize
        for idx, pos in enumerate(cord):
            if idx == i:
                continue
            
            max_x = max(max_x, pos[0])
            max_y = max(max_y, pos[1])
            min_x = min(min_x, pos[0])
            min_y = min(min_y, pos[1])
        square = abs(max_x - min_x) * abs(max_y - min_y)
    min_square = min(min_square, square)


print(min_square)