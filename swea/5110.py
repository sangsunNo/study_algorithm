import sys
sys.stdin = open('input.txt')

case = int(input())


for index in range(case):
    n, m = map(int, input().split())
    numbers = []

    for _ in range(n):
        numbers.append([int(num) for num in input().split()])
    last = numbers[0]

    for t in range(m-1):
        success = 0
        for i, v in enumerate(last):
            if numbers[t+1][0] < v:
                point = i
                last = last[:i] + numbers[t+1] + last[i:]
                success = 1
                # print('success', last)
                break
        if success == 0:
            last = last + numbers[t+1]
            # print('fail', last)
    last.reverse()
    # print(f'{last[:10]}'.replace('[','').replace(']',''))
    # print(','.join(last[-1:-10:-1]))
    # print(*last)
    print(str(last)[1:-1])