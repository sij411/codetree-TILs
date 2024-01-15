n, m = map(int, input().split(" "))
pairs = []
for _ in range(m):
    tp = tuple(map(int, input().split(" ")))
    pairs.append(tp)


def compare(x, y, a, b):
    return x == a and y == b
        
m_cnt = 0
for x, y in pairs:
    cnt = 0
    for a, b in pairs:
        if x < y:
            if a < b and compare(x, y, a, b):
                cnt += 1
            elif a > b and compare(x, y, b, a):
                cnt += 1
        else:
            if a < b and compare(x, y, b, a):
                cnt += 1
            elif a > b and compare(x, y, a, b):
                cnt += 1
    m_cnt = max(cnt, m_cnt)


print(m_cnt)