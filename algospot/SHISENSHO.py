import sys

# call = sys.stdin.readline().strip()
call = 1

for i in range(call):
    # n = sys.stdin.readline().split()
    n = [4, 5]
    # lines = [list(sys.stdin.readline().strip()) for i in range(int(n[0]))]

    lines = [[".", ".", ".", ".", "."], [".", "A", ".", "A", "."], [".", ".", ".", ".", "."], [".", ".", ".", "A", "."],[".", ".", ".", ".", "."]]
    data = {}

    for x, line in enumerate(lines):
        for y, values in enumerate(line):
            if values != '.':
                if values not in data:
                    data[values] = []
                data[values].append([x, y])
    print(data)

    for key in data.keys():
        for i, value in enumerate(data[key]):
            main = value
            for j in range(i+1 ,len(data[key])):
                sub = data[key][i+1]
                print(main, sub)
            print()




