import math

n = int(input())

pos=[]
for _ in range(n):
    pos.append(list(map(int, input().strip().split(" "))))


def triangle(a, b, c):
    ax, ay = pos[a]
    bx, by = pos[b]
    cx, cy = pos[c]

    abx, aby = abs(ax-bx), abs(ay-by)
    acx, acy = abs(ax-cx), abs(ay-cy)
    bcx, bcy = abs(bx-cx), abs(by-cy)

    if aby == 0 and bcx == 0:
        size = abx * bcy * 0.5 * 2
    elif aby == 0 and acx == 0:
        size = abx * acy * 0.5 * 2
    elif bcy == 0 and abx == 0:
        size = bcx * aby * 0.5 * 2
    elif bcy == 0 and acx == 0:
        size = bcx * acy * 0.5 * 2
    elif acy == 0 and bcx == 0:
        size = acx * bcy * 0.5 * 2
    elif acy == 0 and abx == 0:
        size = abx * bcy * 0.5 * 2
    else:
        size = 0
    
    return int(size)

max_size = -math.inf
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            max_size = max(max_size, triangle(i,j,k))
print(max_size)