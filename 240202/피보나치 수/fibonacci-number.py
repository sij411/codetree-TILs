# n번쨰까지 구해야함
n = int(input())

fibo = [-1] * (n + 1)

fibo[1] = 1
fibo[2] = 1

for i in range(3, n + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[n])