x, y = map(int, input().split(" "))

# 자릿수 나누기
max_sum = 0
for num in range(x, y+1):
    cnt = 0
    
    while num > 10:
        r = num%10
        cnt += r
        num //= 10

    cnt += num
    max_sum = max(cnt, max_sum)

print(max_sum)