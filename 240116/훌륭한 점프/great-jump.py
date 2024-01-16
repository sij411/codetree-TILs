n, k = map(int, input().split(" "))

arr = list(map(int, input().split(" ")))

def is_possible(maximum):
    available = [i for i, elem in enumerate(arr) if elem <= maximum]
    for i in range(1, len(available)):
        dist = available[i] - available[i - 1]
        if dist > 2:
            return False
    return True


min_in_max = max(arr) + 1

for a in range(max(arr[0], arr[-1]), max(arr) + 1):
    if is_possible(a):
        min_in_max = min(min_in_max, a)


print(min_in_max)