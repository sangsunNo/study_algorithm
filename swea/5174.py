import sys
sys.stdin = open('input.txt')

def subtree(root):
    global cnt
    cnt += 1

    for i in arr[root]:
        if i:
            subtree(i)
    return cnt



case = int(input())
for _ in range(case):
    cnt = 0
    E, N = map(int, input().split())

    tmp_arr = list(map(int, input().split()))
    arr = [[] for _ in range(E + 2)]

    for i in range(0, len(tmp_arr), 2):
        arr[tmp_arr[i]].append(tmp_arr[i + 1])

    print('ans', subtree(N))


