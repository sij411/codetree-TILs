arr = list(map(int, input().strip().split(" ")))

cnt = 0
for i in range(len(arr)):
    if i <= 1 and (arr[i] >= arr[2] and arr[i] <= arr[3]):
        cnt += 1
    elif i > 1 and (arr[i] >= arr[0] and arr[i] <= arr[1]):
        cnt += 1

if cnt > 0:
    print("intersecting")
else:
    print("nonintersecting")