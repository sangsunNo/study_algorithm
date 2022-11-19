import sys

num = sys.stdin.readline().strip()
num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10}

rev_dect = {}
for key, value in num_dict.items():
    rev_dect[value] = key

for i in range(int(num)):
    break_point = 0
    init = sys.stdin.readline().strip().split()
    if init[1] == "+":
        answer = num_dict[init[0]] + num_dict[init[2]]
    elif init[1] == "-":
        answer = num_dict[init[0]] - num_dict[init[2]]
    elif init[1] == "*":
        answer = num_dict[init[0]] * num_dict[init[2]]
    if answer > 10 or answer < 0:
        print("No")
        continue

    if len(rev_dect[answer]) != len(init[4]):
        break_point = 1
    else:
        for j in rev_dect[answer]:
            if rev_dect[answer].count(j) == init[4].count(j):
                pass
            else:
                break_point = 1
    if break_point == 0:
        print("Yes")
    else:
        print("No")
