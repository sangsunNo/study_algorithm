import sys

# sys.stdin = open('input.txt')

rounds = int(input())

for round in range(1, rounds + 1):
    numbers = list(map(int, input().split()))

    sum_all = 0

    for number in numbers:
        if number % 2 != 0:
            sum_all += number

    # print(f'#{round} {sum_all}')
    print('#{} {}'.format(round, sum_all))