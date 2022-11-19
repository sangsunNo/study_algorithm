count = int(input())

for c in range(count):
    odd_list = []
    even_list = []
    word = input()
    for num, i in enumerate(word):
        if num % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(''.join(even_list) + ''.join(odd_list))
