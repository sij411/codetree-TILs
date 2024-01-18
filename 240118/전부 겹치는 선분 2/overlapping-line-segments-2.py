n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split(" "))))

def out_of_range(a, b, x, y):
    if a == x and b == y:
        return True
    return b < x or y < a 
    
def check():
    for i in range(n): # i 해당 선분 없는 경우
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == j or k == i:
                    continue
                a, b = arr[j] # unpack
                if out_of_range(a, b, arr[k][0], arr[k][1]):
                        cnt += 1
        if cnt == 0 :
            return True
    return False

if check():
    print("Yes")
else:
    print("No")