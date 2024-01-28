n, t = map(int, input().split(" "))
arr = []
for _ in range(3):
    arr.extend(list(map(int, input().strip().split(" "))))


length = len(arr)

for _ in range(t):
    tmp = arr[0]
    for i in range(length - 1, 0, -1):
        move = (i + 1)%(length)
        arr[move] = arr[i] 
    arr[1] = tmp
    
for i in range(length):
    if i > 0 and i % n == 0:
        print()
    print(arr[i], end=" ")