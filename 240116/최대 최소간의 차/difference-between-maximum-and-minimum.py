import sys

n, k = map(int, input().split(" "))

arr = list(map(int, input().strip().split(" ")))


def calculate(k,min_num, max_num): 
    min_cost = sys.maxsize
    cost = 0
    for elem in arr:
        if elem == max_num or elem == min_num:
            continue
        if elem < min_num:
            cost += abs(min_num - elem)
        elif elem > max_num:
            cost += abs(max_num - elem)
    min_cost = min(cost, min_cost)
    return min_cost # 해당 k 한정
        

min_cost = sys.maxsize    
cost_ = 0
for i in range(k+1):
    for elem in arr:
        cost_ = calculate(i, elem, elem+i)
        min_cost = min(cost_, min_cost)

print(min_cost)