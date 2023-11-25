# input
n = int(input())
max_num = 0
bars = []

for i in range(n):
    start, end = map(int, input().split())
    bars.append([start, end])
    if end > max_num:
        max_num = end

# overwrapped
overwrapped = [0 for time in range(max_num+1)] 

# check bar and increment value if bar passed the value of the line 
for bar in bars:
    start, end = bar[0], bar[-1]
    for i in range(start, end+1):
        overwrapped[i] += 1

result = max(overwrapped)
print(result)