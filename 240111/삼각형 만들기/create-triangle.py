import math

n = int(input())

pos=[]
for _ in range(n):
    pos.append(list(map(int, input().strip().split(" "))))


def triangle(a, b, c):
    ax, ay = pos[a]
    bx, by = pos[b]
    cx, cy = pos[c]

    if ay == by and cx == ax: # y parallel
        size = abs(ax-bx) * abs(ay-cy) / 2 * 2
    elif ay == by and cx == bx:
        size = abs(ax-bx) * abs(by-cy) / 2 * 2
    elif ay == cy and bx == ax:
        size = abs(ax-cx) * abs(ay-by) / 2 * 2
    elif ay == cy and bx == cx:
        size = abs(ax-cx) * abs(ay-by) / 2 * 2
    elif by == cy and ax == cx:
        size = abs(bx-cx) * abs(ay-cy) / 2 * 2
    elif by == cy and ax == bx:
        size = abs(bx-cx) * abs(ay-by) / 2 * 2
    else:
        size = 0


    
    
    return int(size)

max_size = -math.inf
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            max_size = max(max_size, triangle(i,j,k))
print(max_size)