import sys

num = int(input())

for i in range(num):
    three = []
    x = 0
    y = 0
    for j in range(3):
        three.append(sys.stdin.readline().strip().split())
    if three[0][0] == three[1][0]:
        x = three[2][0]
    elif three[1][0] == three[2][0]:
        x = three[0][0]
    else:
        x = three[1][0]

    if three[0][1] == three[1][1]:
        y = three[2][1]
    elif three[1][1] == three[2][1]:
        y = three[0][1]
    else:
        y = three[1][1]

    print(x, y)
