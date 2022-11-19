import sys
sys.stdin = open('input.txt')

case = int(input())

for round in range(1, case + 1):
    count = int(input())
    numbers = list(map(int, input().split()))
    money = 0
    for index, buy_number in enumerate(numbers):
        sell_time = 0
        for sell_number in range(index + 1, len(numbers)):
            sell_price = numbers[sell_number]
            if buy_number < sell_price and sell_price > sell_time:
                sell_time = sell_price
        if sell_time != 0:
            money += sell_time - buy_number
    print('#{} {}'.format(round, money))
