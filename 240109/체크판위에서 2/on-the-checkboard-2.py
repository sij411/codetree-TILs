r, c = map(int, input().split(' '));


grid = []
for _ in range(r):
    grid.append(input().split(' '))


cnt = 0
for i in range(1, r):
    for j in range(1, c):
        for k in range(i+1, r):
            for l in range(j+1, c):
                if grid[0][0] =='B' and grid[i][j] == 'W' and grid[k][l] == 'B':
                    for a in range(k+1, r):
                        for b in range(l+1, c):
                            if (a == r-1 and b == c-1) and grid[a][b] == 'W':
                                cnt += 1
                elif grid[0][0] =='W' and grid[i][j] =='B' and grid[k][l] == 'W':
                    for a in range(k+1, r):
                        for b in range(l+1, c):
                            if (a == r-1 and b == c-1) and grid[a][b] == 'B':
                                cnt += 1

print(cnt)