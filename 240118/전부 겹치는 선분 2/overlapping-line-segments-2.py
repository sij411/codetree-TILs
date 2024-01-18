n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split(" "))))

arr.sort()
def check():
    cnt = 0
    st, end= 0, 0
    while st <= n-1 and end <= n-1:
        if arr[st][0] <= arr[end][1]:
            st += 1
            cnt += 1
        elif arr[st][0] > arr[end][1]:
            cnt -= 1
            end += 1
        if cnt >= n-1:
            return True
    return False

if check():
    print("Yes")
else:
    print("No")