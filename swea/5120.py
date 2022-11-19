import sys
sys.stdin = open('input.txt')

case = int(input())

for index in range(case):
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    start = 0
    
    for _ in range(k):
        start = (start + m) % n
        if start:
            numbers.insert(start, numbers[start - 1] + numbers[start])
        else:
            numbers.insert(numbers[-1], numbers[-1] + numbers[0])
            start -= 1
        # print(numbers)






        n += 1

    list.reverse(numbers)
    print(numbers[:10])
    # break
