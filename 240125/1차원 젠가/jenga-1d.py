n = int(input())

arr = [int(input()) for _ in range(n)]

will_delete = []
for _ in range(2):
    will_delete.append(tuple(map(int, input().split(" "))))

# delete
# 얘 때문에 오래 걸리는듯. 
def make_blank(arr, st, end):
    for i in range(st, end+1):
        arr[i] = 0

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
   

cnt = len(arr)

print(cnt)

for i in range(len(arr)):
    print(arr[i])