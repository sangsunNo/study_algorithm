import sys

case = sys.stdin.readline().strip()
# case = 100

for c in range(int(case)):
    data = sys.stdin.readline().strip()
    data = list(data)
    # data = "0100011"
    block_list = [[0, 2, 4, 6], [1, 2, 5, 6], [3, 4, 5, 6]]
    answer = ""
    save = 0
    xor = 0
    for i in block_list:
        save = 0
        for index, j in enumerate(i):
            if index == 0:
                save = int(data[j])
                # print('inti_savd ', save)
                continue
            # print("befre : save", save, "data", int(data[j]))
            save = save ^ int(data[j])
            # print("after =", save)
        answer += str(save)
        # print('ans', answer)
        # print('-------------')
    wrong_num = int(answer[::-1], 2)-1
    # print('t', data)
    # print('w', wrong_num)
    if wrong_num < 0:
        pass
    else:
        if data[wrong_num] == '0':
            data[wrong_num] = '1'
        else:
            data[wrong_num] = "0"
    fin = ""
    fin = data[2] +data[4] +data[5] +data[6]
    # print(data)
    # print(data[6])
    print(fin)