point = 0
x = int(input())
y = int(input())
x_y = [0, 0]
direction = input()
if x == 0 and y == 0:
    print(0)
while direction != 'стоп':
    steps = int(input())
    point += 1
    if direction == 'север':
        x_y[1] += steps
    elif direction == 'запад':
        x_y[0] -= steps
    elif direction == 'юг':
        x_y[1] -= steps
    elif direction == 'восток':
        x_y[0] += steps
    if int(x) == x_y[0] and int(y) == x_y[1]:
        print(point)
        break
