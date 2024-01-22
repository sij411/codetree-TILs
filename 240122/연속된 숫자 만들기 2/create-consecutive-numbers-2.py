a, b, c = map(int, input().strip().split(" "))

all_seq = False


def check_seq(a, b, c):
    if (a + 1) == b and (b + 1) == c:
        all_seq = True
    return all_seq

all_seq = check_seq(a, b, c)


if all_seq:
    cnt = 0
else:
    if (b - a) == 2 or (c - b) == 2:
        cnt = 1
    else:
        cnt = 2

print(cnt)