import sys
sys.stdin = open('input.txt')

case = int(input())

for index in range(case):
    n, m, l = map(int, input().split())
    numbers = [int(num) for num in input().split()]
    for _ in range(m):
        i, v = map(int, input().split())
        numbers.insert(i, v)
    print(numbers[l])
    # break
