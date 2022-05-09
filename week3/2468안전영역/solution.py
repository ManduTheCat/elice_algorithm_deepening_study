import sys
from collections import deque
def make_safe_map(map, h):
	n = len(map)
	safe_map=[[False for _  in range(n)] for _ in range(n)]
	for row in range(n):
		for col in range(n):
			if map[row][col] <= h: # 낮은 지대라면 True 높은 지대라면 false 로만들어
				# bfs 로 False 인부분을 찾는다 즉 높은 부분 그룹을 찾는다
				safe_map[row][col] = True
			else: safe_map[row][col]= False
	return safe_map

def count_map(map, h):
	safe_map = make_safe_map(map, h)
	count = 0
	for i,row in enumerate(safe_map):
		for j,val in enumerate(row):
			if val == False:
				count +=1
				bfs(safe_map, i,j)
	return count

def bfs(safe_map, i,j):
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	q = deque()
	q.append([i,j])
	while(q):
		cur_node = q.popleft()
		for i in range(len(dx)):
			try:
				next_node = [cur_node[0]+dx[i],cur_node[1]+dy[i]]
				next_node_value = safe_map[next_node[0]][next_node[1]]
				if (next_node[0] != -1) and (next_node[1] != -1) and next_node_value == False:
					safe_map[next_node[0]][next_node[1]] = True
					q.append([next_node[0], next_node[1]])
			except:
				continue

def main():
	# 입력
	size = int(input())
	rain_map = []
	for _ in range(size):
		n_row = list(map(int, sys.stdin.readline().strip().split(" ")))
		rain_map.append(n_row)

	# 결과
	count = [1] # 비가 안오는 경우 안전지대는 1인경우를 생각하면 무조건 1은 나온다.
	for h in range(1, 101):
		count.append(count_map(rain_map, h))
	print(max(count))

if __name__ == "__main__":
	main()
