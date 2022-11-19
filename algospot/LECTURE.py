num = input()

for s in range(int(num)):
    s = input()
    str_temp = []
    for num in range(len(s)):
        if num % 2 == 1:
            continue
        str_temp.append(s[num:num+2])
    str_temp.sort()
    print(''.join(str_temp))