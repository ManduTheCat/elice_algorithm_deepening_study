n = int(input())
vps = []

for _ in range(n):
    ps = input()
    tetris = []

    for parenthesis in ps:
        if tetris:
            if parenthesis==tetris[-1]:
                tetris.append(parenthesis)
            else:
                if parenthesis==')':
                    tetris.pop()
        else:
            tetris.append(parenthesis)
    
    if tetris:
        vps.append('NO')
    else:
        vps.append('YES')
        
print(*vps, end='\n')