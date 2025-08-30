import sys

lines = sys.stdin.readlines()
k = int(lines[0])
word = lines[1]

if "lv" in word:
    print(0)
    exit()

arr_word = list(word)
for x in range(k):
    if arr_word[x] == "l" and x < k - 1:
        arr_word[x + 1] = "v"
        print(1)
        exit()
    elif arr_word[x] == "v" and x > 0:
        arr_word[x - 1] = "l"
        print(1)
        exit()

arr_word[0] = "l"
arr_word[1] = "v"
print(2)
