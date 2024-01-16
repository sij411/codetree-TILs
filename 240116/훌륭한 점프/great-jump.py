n, k = map(int, input().split(" "))

arr = list(map(int, input().split(" ")))

def is_possible(maximum):
    available = [i for i, elem in enumerate(arr) if elem >= maximum]
    for i in range(1, len(available)):
        dist = available[i] - available[i - 1]
        if dist > 2:
            return False
    return True


min_in_max = 0

for a in range(n - 1, -1, -1):
    if is_possible(a):
        min_in_max = max(min_in_max, a)


print(min_in_max)