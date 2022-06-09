from math import sqrt

M, N = int(input()), int(input())

checklist = list(range(M, N+1))
answer = []

for num in checklist:
    if sqrt(num).is_integer():
        answer.append(num)

if(len(answer)==0):
    print(-1)
else:
    print(sum(answer))
    print(answer[0])