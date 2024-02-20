a, b, c = map(int, input().strip().split(" "))


def check_seq(a, b, c):
    if (a + 1) == b and (b + 1) == c:
        return True
    return False



if check_seq(a, b, c):
    cnt = 0
else:
    if (b - a) == 2 or (c - b) == 2:
        cnt = 1
    else:
        cnt = 2

print(cnt)