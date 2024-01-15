n = int(input())
seats_pos = input()


max_distance = 0
for i in range(n):
    
    if seats_pos[i] != '0':
        continue
    cur_nearest_d = n
    nearest_idx = i
    for seat in range(n):
        if seat != i and seats_pos[seat] == '1' and abs(i-seat) < cur_nearest_d:
            cur_nearest_d = abs(i-seat)
            nearest_idx = seat
    max_distance = max(abs(nearest_idx - i), max_distance)
print(max_distance)