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

def gravity(arr):
    end_of_arr = len(arr)
    _arr = [0] * end_of_arr
    temp = [0] * end_of_arr # end of array
    end_of_temp_arr = 0
    for i in range(end_of_arr):
        if arr[i] != 0:
            temp[end_of_temp_arr] = arr[i]
            end_of_temp_arr +=1

    for i in range(end_of_temp_arr):
        _arr[i] = temp[i]
    
    return _arr




# output 
# 남은 블록 개수 len(arr)
# 그 숫자들 arr 

for elem in will_delete:
    arr = make_blank(arr, elem[0]-1, elem[1]-1)
    arr = gravity(arr)
  
cnt = 0
for i in range(len(arr)):
    if arr[i] != 0:
        cnt += 1

print(cnt)

for i in range(len(arr)):
    if arr[i] != 0:
        print(arr[i])