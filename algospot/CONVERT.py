import sys

num = int(input())

for i in range(num):
    word = sys.stdin.readline().strip().split()
    if word[1] == "kg":
        word[0] = float(word[0]) * 2.2046
        word[1] = "lb"
    elif word[1] == "l":
        word[0] = float(word[0]) * 0.2642
        word[1] = "g"
    elif word[1] == "lb":
        word[0] = float(word[0]) * 0.4536
        word[1] = "kg"
    elif word[1] == "g":
        word[0] = float(word[0]) * 3.7854
        word[1] = "l"

    print("{0} {1:.4f} {2}".format(i+1, word[0], word[1]))
