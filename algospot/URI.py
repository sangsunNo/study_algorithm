import sys

num = sys.stdin.readline().strip()
encod_dic = {"20" : " ", "21" : "!", "24" : "$", "25" : "%", "28" : "(", "29" : ")", "2a" : "*"}

for n in range(int(num)):
    uri = sys.stdin.readline().strip()
    ch_word = ''
    sur_split = uri.split("%")
    for index, word in enumerate(sur_split):
        if index == 0:
            ch_word += word
        else:
            ch_word += word[:2].replace(word[:2], encod_dic[word[:2]])
            ch_word += word[2:]
    print(ch_word)
