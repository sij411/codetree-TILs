import sys

n, k = map(int, input().split(" "))

arr = list(map(int, input().strip().split(" ")))

# find max min pairs
def find_max_min_pairs(k):
    arr = []
    for a in range(10000):
        for b in range(10000):
            if a - b == k:
                arr.append((a, b))
    return arr

def calculate(k): 
    pairs = find_max_min_pairs(k)
    min_cost = sys.maxsize
    for max_num, min_num in pairs:
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

for i in range(k+1):
    cost = calculate(i)
    min_cost = min(cost, min_cost)

print(min_cost)