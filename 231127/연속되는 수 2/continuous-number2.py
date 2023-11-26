total_num = int(input())
nums = []

for i in range(total_num):
    num = int(input())
    nums.append(num)

cnt = 0

for i in range(total_num):
    if i == 0 or nums[i] == nums[i-1]:
        cnt += 1

print(cnt)