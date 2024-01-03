'''
 input : 
    N: how many times
    L : anti-clockwise = True 
    R : clockwise = True
    F : current direction (== previous direction)
'''

dir_num = 0 # north
cur_x = 0
cur_y = 0
# (default) clockwise: 0 north 1 east 2 south 3 west
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

def anti_clockwise(dir_num): # L
    return (dir_num - 1 + 4) % 4

def clockwise(dir_num): # R
    return (dir_num + 1) % 4

def front(dir_num, cur_x, cur_y): # F
    cur_x += x[dir_num]
    cur_y += y[dir_num]
    return cur_x, cur_y

def set_dir(command, dir_num):
    if command == 'L':
        return anti_clockwise(dir_num)
    elif command == 'R':
        return clockwise(dir_num)
    return dir_num

def move(command, dir_num, cur_x, cur_y):
    if command == 'F':
        return front(dir_num, cur_x, cur_y)
    return cur_x, cur_y

string = input()
n = len(string)

for i in range(n):
    command = string[i]
   # print(command)
    if command == 'F':
        cur_x, cur_y = move(command, dir_num, cur_x, cur_y)
    else:
        dir_num = set_dir(command, dir_num)

print(cur_x, cur_y)