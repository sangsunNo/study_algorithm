import sys

sys.stdin = open('input.txt')

case = int(input())

for count in range(1, case + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    leaf = []
    for _ in range(M):
        leaf.append(list(map(int, input().split())))
    for index, value in leaf:
        tree[index] = value
        while index // 2 > 0:
            tree[index // 2] += value
            index = index // 2
    print(tree[L])




