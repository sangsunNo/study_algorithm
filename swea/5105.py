import sys

sys.stdin = open('input.txt')
case = int(input())

def bfs(s_x, s_y):
    print('new')
    q = []
    visited = []

    num = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q.append((s_x, s_y))
    visited.append((s_x, s_y))
    while q:
        s_x, s_y = q.pop(0)


        for t_x, t_y in num:
            x = s_x + t_x
            y = s_y  + t_y
            if 0 <= x < 5 and 0 <= y < 5 and (x, y) not in visited and maze[x][y] != 1:
                distance[x][y] = distance[s_x][s_y] + 1
                q.append((x, y))
                if maze[x][y] == 3:
                    return distance[s_x][s_y]
            else:
                visited.append((s_x, s_y))





for index in range(1, case + 1):
    maze = []
    size = int(input())

    for _ in range(size):
        maze.append(list(map(int, input())))

    for x in range(size):
        for y in range(size):
            if maze[x][y] == 2:
                s_x, s_y = x, y



    distance = [[0] * size for _ in range(size)]
    print(f'#{index} {bfs(s_x, s_y)}')
    # break