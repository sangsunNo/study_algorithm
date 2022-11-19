import sys

num = int(input())

for i in range(num):
    word = sys.stdin.readline().strip().split()
    print(i+1, word[1][0:int(word[0])-1] + word[1][int(word[0]):])