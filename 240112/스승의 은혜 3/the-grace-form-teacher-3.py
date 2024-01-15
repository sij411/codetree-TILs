# input: students, budget
import copy

n, budget = map(int, input().strip().split(" "))

students = []
for _ in range(n):
    students.append(list(map(int, input().split(" "))))

# print(students)

def calculate(discount_idx):
    total = 0
    cnt = 0
    arr = copy.deepcopy(students)
    arr[discount_idx][0] /= 2
    arr_sorted = sorted(arr, key=c_sort)
    # print(arr_sorted)
    for idx, order in enumerate(arr_sorted):
        price, shipping = order[0], order[1]
        if (total + price + shipping) > budget:
            return total, cnt
        # print(total, "??")
        cnt += 1
        total += price + shipping
        # print(discount_idx, total, cnt)
    return total, cnt

def c_sort(item):
    return item[0] + item[1]

max_cnt = -1

for i in range(n):
    total, cnt = calculate(i)
    # print(i, total, cnt)
    if total <= budget:
        max_cnt = max(max_cnt, cnt)

print(max_cnt)