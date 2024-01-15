import sys

n = int(input())
a_list = []
b_list = []
for _ in range(n):
    a, b = map(int, input().split(" "))
    a_list.append(a)
    b_list.append(b)

def check(x):
    x_ = 2 * x
    for a, b in zip(a_list, b_list):
        if a <= x_ <= b:
            x_ = 2 * x_
        else:
            return False
    return True


min_x = sys.maxsize

for x in range(1, 5001):
    if check(x):
        min_x = min(x, min_x)
    
    
print(min_x)