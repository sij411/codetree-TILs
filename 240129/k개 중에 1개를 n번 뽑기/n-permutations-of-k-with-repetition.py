k, n = map(int, input().split(" "))

arr = []
cnt = 0

def print_pair(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def choose(curr_count):
    global cnt
    if curr_count == k:
        cnt += 1
        print_pair(arr)
        return 
    for i in range(n):
        arr.append(i + 1)
        choose(curr_count + 1)
        arr.pop()

choose(0)