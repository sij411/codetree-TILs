k, n = map(int, input().split(" "))

arr = []


def print_pair(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def choose(curr_count):
    
    if curr_count == n:
        print_pair(arr)
        return 
        
    for i in range(k):
        arr.append(i + 1)
        choose(curr_count + 1)
        arr.pop()

choose(0)