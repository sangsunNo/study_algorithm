import sys

num = sys.stdin.readline().strip()

for i in range(int(num)):
    limit = sys.stdin.readline().strip()
    use_time = sys.stdin.readline().strip().split()
    sum_use = 0

    for h_use in use_time:
        sum_use += int(h_use)
    if int(limit) >= sum_use:
        print("YES")
    else:
        print("NO")