total_num = int(input())
nums = []

for i in range(total_num):
    num = int(input())
    nums.append(num)

cnt = 0
maximum = 0

for i in range(total_num):
    if i >= 1 and nums[i] == nums[i-1]:
        cnt += 1
    else:
        cnt = 1
    maximum = max(cnt, maximum) 

print(maximum)