import sys

sys.stdin = open('input.txt')

case = int(input())

for index in range(case):
    q = []

    whaduck_size, len_pizze = list(map(int, input().split()))
    cheeze = list(enumerate(map(int, input().split())))

    for i in range(whaduck_size):
        q.append(cheeze[0])
        cheeze.pop(0)

    while len(q) > 1:
        check = list (q.pop(0))
        check[1] //= 2
        if check[1] == 0:
            if cheeze:
                q.append(cheeze.pop(0))
        else:
            q.append(check)

    print(f'#{index} {q[0][0]+1}')


