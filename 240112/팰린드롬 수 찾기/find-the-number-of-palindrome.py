x, y = map(int, input().split(" "))

cnt = 0
for num in range(x, y + 1):
    reverse = 0
    temp = num
    while temp > 0:
        reverse = (reverse * 10) + temp%10
        temp = temp//10
    if reverse == num:
        cnt += 1    

print(cnt)