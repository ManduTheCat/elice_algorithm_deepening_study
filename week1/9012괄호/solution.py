def isRight(s):
    while True:
        s = s.replace("()", "")
        if "()" not in s:
            if s: return "NO"
            else: return "YES"

T = int(input())
for i in range(T):
    strings = input()
    print(isRight(strings))