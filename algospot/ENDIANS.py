import sys

for i in range(int(sys.stdin.readline())):
    c_num = []
    number = 0
    val = sys.stdin.readline().strip()
    val = hex(int(val)).replace('0x', '').zfill(8)
    for num in range(len(val)):
        if num % 2 == 1:
            continue
        c_num.append(val[num:num + 2])
    c_num = c_num[::-1]
    number = '0x'+''.join(c_num)
    number = int(number, 16)
    print(number)