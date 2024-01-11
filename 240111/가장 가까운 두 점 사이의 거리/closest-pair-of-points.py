import sys
# input : the number of coordinations 
n = int(input())

coords = []
for _ in range(n):
    coord = list(map(int, input().split(" ")))
    coords.append(coord)

# 거리의 제곱: (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
min_f, min_s, min_d = sys.maxsize, sys.maxsize, sys.maxsize
for i in range(n): # first dot
    for j in range(i+1, n): # second dot 
        x1, y1 = coords[i][0], coords[i][1] # first
        x2, y2 = coords[j][0], coords[j][1] # second
        d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        if min_d > d:
            min_d = d
            min_f, min_s = coords[i], coords[j]

print(min_d)