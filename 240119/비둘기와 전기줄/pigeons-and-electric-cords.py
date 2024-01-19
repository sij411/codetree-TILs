n = int(input())

pigeons = [[] for _ in range(11)]

for _ in range(n):
    idx, d = map(int, input().strip().split(" "))
    pigeons[idx].append(d)

cnt = 0
for p, move in enumerate(pigeons):
    if len(move) < 2:
        continue
    for m in range(1, len(move)):
        if move[m] != move[m-1]:
            cnt += 1

print(cnt)