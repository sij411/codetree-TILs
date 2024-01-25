n = int(input())

arr = [int(input()) for _ in range(n)]

will_delete = []
for _ in range(2):
    will_delete.append(tuple(map(int, input().split(" "))))

# delete

def make_blank(arr, st, end):
    for i in range(st, end+1):
        arr[i] = 0
    return arr


# 좀 오래 걸려서 시간 단축하는 방법으로 좀 줄여보면 좋겠음. 
def gravity(arr):
    end_of_arr = len(arr)
    temp = [] # end of array

    for i in range(end_of_arr):
        if arr[i] != 0:
            temp.append(arr[i])

    return temp




# output 
# 남은 블록 개수 len(arr)
# 그 숫자들 arr 

for elem in will_delete:
    arr = make_blank(arr, elem[0]-1, elem[1]-1)
    arr = gravity(arr)

cnt = len(arr)

print(cnt)

for i in range(len(arr)):
    print(arr[i])