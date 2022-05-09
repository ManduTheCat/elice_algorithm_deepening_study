n, k = map(int, input().split(' '))
medal_list = []
rank, cnt = 1, 0 # 1위부터 순위 매기는데 제일 앞에 있는 국가가 1순위, 동점 카운트 추가

def find_rank(country):
    global rank, cnt
    if sorted_medal_list[0][0] == country: # 첫 국가가 찾는 국가이면
        return rank # 1을 출력
        
    for i in range(1, n):
        if (sorted_medal_list[i - 1][1] == sorted_medal_list[i][1]) and (sorted_medal_list[i - 1][2] == sorted_medal_list[i][2]) and (sorted_medal_list[i - 1][3] == sorted_medal_list[i][3]): # 이전 국가와 금은동 메달 수가 같을 때
            # print('동점 발생')
            cnt += 1  
            if sorted_medal_list[i][0] == country:
                # 찾는 국가이면 이전 국가와 동일한 랭크를 출력
                return rank 
                
        else: # 이전 국가와 메달 수가 하나라도 다르면 
            # print('동점 없음')
            rank += 1 # 기본 랭크 1 증가
            rank += cnt # 랭크에 동점카운트도 반영
            cnt = 0 # 동점 카운트는 다시 0으로
        
            if sorted_medal_list[i][0] == country: # 찾는 국가이면
                return rank # 해당 국가의 랭크를 동점 카운트를 추가해서 출력

for i in range(n):
    medal_list.append(list(map(int, input().split(' '))))

sorted_medal_list = sorted(medal_list, key = lambda x: [x[1], x[2], x[3]], reverse=True)
# print(sorted_medal_list)
print(find_rank(k))