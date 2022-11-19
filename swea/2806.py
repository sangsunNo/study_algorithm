import sys
sys.stdin = open('input.txt')

# info = 1 값이 들어있는 행
# count = 현재 행 위치

def check(info, count):
    global cnt
    room = [0] * N

    if count == N:
        cnt += 1
        return

    # 못가는 곳 설정 room
    for index in range(len(info)):
        room[info[index]] = 1
        if info[index] - (count - index) >= 0:
            room[info[index] - (count - index)] = 1
        if info[index] + (count - index) < N:
            room[info[index] + (count - index)] = 1

    # print(room)
    # 내가 들어갈 방
    for j in range(N):
        if 1 != room[j]:
            check(info + [j], count + 1)





for tc in range(int(input())):
    N = int(input())
    cnt = 0
    check([], 0)
    print("#{} {}".format(tc+1, cnt))