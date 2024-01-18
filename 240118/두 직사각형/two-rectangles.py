x1, y1, x2, y2 = map(int, input().strip().split(" "))

a1, b1, a2, b2 = map(int, input().strip().split(" "))
ab = [a1, b1, a2, b2]

cnt = 0
if y2 < b1:
    cnt += 1
if x2 < a1:
    cnt += 1
if y1 > b2:
    cnt += 1
if a2 < x1:
    cnt += 1


if cnt > 0:
    print("nonoverlapping")
else:
    print("overlapping")