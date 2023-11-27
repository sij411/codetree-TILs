n, m = map(int, input().split())

a_rec = [0]
a_loc = 0   # current a loc

for i in range(n):
    d, t = input().split()
    for i in range(int(t)):
        if d == "R":
            a_loc += 1
        else:
            a_loc -= 1

        a_rec.append(a_loc)

b_rec = [0]
b_loc = 0

for i in range(m):
    d, t = input().split()
    for i in range(int(t)):
        if d == "R":
            b_loc += 1
        else:
            b_loc -= 1

        b_rec.append(b_loc)


# check 

result = -1 

for i in range(1, len(a_rec)):
    if a_rec[i] == b_rec[i]:
        result = i
        break
    else:
        result = -1

        
print(result)