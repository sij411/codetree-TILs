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
        if (x == a and y == b) or (x == b and y == a):
            cnt += 1
    m_cnt = max(cnt, m_cnt)


print(m_cnt)