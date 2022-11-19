import sys
sys.stdin = open('input.txt')


def bfs(s, g):
    q.append(s)
    print(line)
    while q:
        s = q.pop(0)
        print('s', s)
        for i in line:
            if s == i[0]:
                if visited[i[1]] == True:
                    continue
                else:
                    visited[i[1]] = True
                    q.append(i[1])
                    print('find', i[1])
                    count[i[1]] = count[i[0]] + 1
                    if i[1] == g:
                        print('fin')
                        return count[i[1]]
        print(q)
        print(count)
        print()


# 1 -> 4 -> 6




case = int(input())

for index in range(1, case + 1):
    # v = 노드 갯수
    # e = 간선 갯수

    v, e = map(int, input().split())
    line = []
    count = [0] * (v + 1)
    visited = [False] * (v + 1)
    q = []

    for i in range(e):
        line.append(list(map(int, (input().split()))))
    for j in range(len(line)):
        line.append([line[j][1], line[j][0]])
    s, g = map(int, input().split())
    print(index, 'asb', bfs(s, g))
