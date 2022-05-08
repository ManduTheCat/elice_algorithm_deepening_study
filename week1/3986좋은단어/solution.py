n = int(input())
good_word = 0

for _ in range(n):
    word = input()
    tetris = []

    for alphabet in word:
        if tetris:
            if alphabet==tetris[-1]:
                tetris.pop()
            else:
                tetris.append(alphabet)
        else:
            tetris.append(alphabet)
    
    if not tetris:
        good_word += 1

print(good_word)