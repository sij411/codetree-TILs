# input: students, budget

n, budget = map(int, input().strip().split(" "))

students = []
for _ in range(n):
    students.append(list(map(int, input().split(" "))))


def calculate(discount_idx, students):

    total = 0
    cnt = 0
    for idx, order in enumerate(students):
        if idx == discount_idx:
            price, shipping = order[0]//2, order[1]
        else:
            price, shipping = order[0], order[1]
        
        if (total + price + shipping) <= budget:
            total += (price + shipping)
            cnt += 1
        else:
            return total, cnt
    return total, cnt

def c_sort(item):
    return item[0] + item[1]

max_cnt = 0
arr_sorted = sorted(students, key=c_sort)
for i in range(n):
    total, cnt = calculate(i, arr_sorted)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)