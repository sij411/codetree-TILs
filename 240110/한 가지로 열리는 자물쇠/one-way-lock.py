n = int(input())
given = list(map(int, input().strip().split(" ")))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            
            if (abs(i-given[0]) > 2) and (abs(j-given[1]) > 2) and (abs(k-given[2]) > 2) :
                # print(f"{i} {j} {k}")
                cnt += 1
                    
total = n**3   
result = total - cnt  
print(total-cnt)