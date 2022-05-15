n = int(input())
word_list = []
for i in range(n):
    word_list.append(input())
word_list = list(set(word_list))
word_list = sorted(word_list)
word_list = sorted(word_list, key = lambda x: len(x))
for word in word_list:
    print(word)