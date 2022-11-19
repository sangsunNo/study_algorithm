import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    maze_range = int((n) / 2)
    len = 1
    money = 0
    left = maze_range
    right = maze_range

    for i, v in enumerate(maze):
        if i <= maze_range:
            for m in range(left, right+1):
                money += v[m]

            if i < maze_range:
                left -= len
                right += len
            else:
                left += len
                right -= len
        else:
            for m in range(left, right+1):
                money += v[m]
            left += len
            right -= len
    print(f'#{tc} {money}')

