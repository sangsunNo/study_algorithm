import sys
sys.stdin = open('input.txt')

case = int(input())

for t in range(case):
    N, M, L = map(int, input().split())
    ans = -1
    arr = list(map(int,input().split()))
    for _ in range(M):
        info = input().split()

        if info[0] == "I":
            arr.insert(int(info[1]), int(info[2]))
        if info[0] == "D":
            arr.pop(int(info[1]))
        else:
            arr[int(info[1])] = int(info[2])
    if L <= len(arr) + 1:
        ans = arr[L]
    print(ans)

