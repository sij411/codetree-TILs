# input: students, budget

n, budget = map(int, input().strip().split(" "))

students = []
for _ in range(n):
    students.append(list(map(int, input().split(" "))))

# print(students)

def calculate(discount_idx):
    total = 0
    cnt = 0
    for idx, order in enumerate(students):
        if total >= budget:
            return total, cnt
        if idx == discount_idx:
            price, shipping = order[0]/2, order[1]
        else:
            price, shipping = order[0], order[1]
        cnt += 1
        total += price + shipping
    return total, cnt

max_cnt = 0
for i in range(n):
    total, cnt = calculate(i)
    cnt = max(max_cnt, cnt)

print(cnt)