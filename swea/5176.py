import sys

sys.stdin = open('input.txt')

def subtree(sub_root):
    global count
    # 배열이니까 배열크기 넘어가지 않도록
    if sub_root <= N:
        subtree(sub_root * 2)
        tree[sub_root] = count
        count += 1
        subtree(sub_root * 2 + 1)

case = int(input())
for _ in range(case):
    N = int(input())
    numbers = [i for i in range(1, N + 1)]
    tree = [[] for _ in range(N + 1)]
    count = 1
    subtree(1)
    print(tree)
    break