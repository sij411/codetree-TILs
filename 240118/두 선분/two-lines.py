arr = list(map(int, input().strip().split(" ")))


for i in range(len(arr)):
    if i <= 1 and (arr[i] >= arr[2] and arr[i] <= arr[3]):
        print("intersecting")
        break
    elif i > 1 and (arr[i] >= arr[0] and arr[i] <= arr[1]):
        print("intersecting")
        break
    else:
        print("nonintersecting")
        break