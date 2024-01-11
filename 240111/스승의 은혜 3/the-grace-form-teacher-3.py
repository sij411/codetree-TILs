# input: students, budget

n, budget = map(int, input().strip().split(" "))

students = []
for _ in range(n):
    students.append(list(map(int, input().split(" "))))

# print(students)

def calculate(discount_idx, students):
    total = 0
    cnt = 0
    for idx, order in enumerate(students):
        if idx == discount_idx:
            price, shipping = order[0]/2, order[1]
        else:
            price, shipping = order[0], order[1]
        if (total + price + shipping) > budget:
            return total, cnt
        cnt += 1
        total += price + shipping
        # print(discount_idx, total, cnt)
    return total, cnt

def c_sort(item):
    return item[0] + item[1]

max_cnt = -1
arr_sorted = sorted(students, key=c_sort)
# print(arr_sorted)
for i in range(n):
    total, cnt = calculate(i, arr_sorted)
    # print(i, total, cnt)
    if total <= budget:
        max_cnt = max(max_cnt, cnt)

print(max_cnt)