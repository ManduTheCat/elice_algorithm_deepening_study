n = int(input())
score_list = []

for i in range(n):
    score_list.append(list(map(str, input().split())))
    score_list[i][1], score_list[i][2], score_list[i][3] = int(score_list[i][1]), int(score_list[i][2]), int(score_list[i][3])


score_list.sort(key=lambda x: [-x[1], x[2], -x[3], x[0]])
for i in range(n):
    print(score_list[i][0])