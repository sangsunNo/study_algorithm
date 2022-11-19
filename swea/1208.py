import sys
sys.stdin = open('input.txt')


tc = 10
def change_l():
    global numbers
    numbers[0] += 1
    for index in range(len(numbers)):
        if numbers[index] < numbers[0]:
            same_num = numbers.count(numbers[index])
            if same_num == 1:
                numbers[index], numbers[0] = numbers[0], numbers[index]
            else:
                numbers[index + same_num - 1], numbers[0] = numbers[0], numbers[index + same_num - 1]



def change_h():
    global numbers
    numbers[-1] -= 1
    for index in range(len(numbers)-1, -1, -1):
        if numbers[index] > numbers[-1]:
            same_num = numbers.count(numbers[index])
            if same_num == 1:
                numbers[index], numbers[-1] = numbers[-1], numbers[index]
            else:
                numbers[index - same_num + 1], numbers[-1] = numbers[-1], numbers[index - same_num + 1]





for i in range(1, tc + 1):
    num = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    for _ in range(num):
        change_h()
        change_l()
        if numbers[-1] - numbers[0] < 2:
            break
    print(f'#{i} {numbers[-1] - numbers[0]}')


