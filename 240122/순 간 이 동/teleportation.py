a, b, x, y = map(int, input().strip().split(" "))

cnt1 = abs(a-b)
cnt2 = abs(a-x) + abs(y-b)
cnt3 = abs(a-y) + abs(x-b)

ans = min(cnt1, cnt2, cnt3)

print(ans)