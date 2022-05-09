"""
입력과 bfs 에 쓰일 deque 를 사용하기 위한 sys, deque
"""
import sys
from collections import deque

def make_safe_map(input_map, rain_h):
    """
     낮은 지대라면 True 높은 지대라면 false 로 이루어진 map 을 반환한는 함수
    """
    len_n = len(input_map)
    safe_map = [[False for _ in range(len_n)] for _ in range(len_n)]
    for row in range(len_n):
        for col in range(len_n):
            if input_map[row][col] <= rain_h:
                safe_map[row][col] = True
            else: safe_map[row][col] = False
    return safe_map

def count_map(input_map, rain_h):
    """
    안전지역 갯수를 세는 함수
    새로운 bfs 를 진입하면 새로운 덩어리임을 활용
    safe_map 에는 위치별로  높이에 따른 안전지대면 false 물에잠기면 true 가 있다.
    """
    safe_map = make_safe_map(input_map, rain_h)
    count = 0
    for i, row in enumerate(safe_map):
        for j, val in enumerate(row):
            if val is False:
                count += 1
                bfs(safe_map, i, j)
    return count

def bfs(safe_map, i, j):
    """
    bfs 를 체크 해서 safe_map 인접한 칸 들을 방문한다
    매개변수로 사용된 safe_map 은 deep copy 를 하지 않았기에 bfs 에서 true 로
    체크가되면 호출된 count_map() 에서의 safe_map 변수 에도 반영된다.
    """
    d_x = [1, -1, 0, 0]
    d_y = [0, 0, 1, -1]
    queue = deque()
    queue.append([i, j])

    while queue:
        cur_node = queue.popleft()
        for itor, _ in enumerate(d_x):
            try:
                next_node = [cur_node[0] + d_x[itor], cur_node[1] + d_y[itor]]
                next_node_value = safe_map[next_node[0]][next_node[1]]
                if (next_node[0] != -1) and (next_node[1] != -1) and next_node_value is False:
                    safe_map[next_node[0]][next_node[1]] = True
                    queue.append([next_node[0], next_node[1]])
            except IndexError:
                continue

def main():
    """
    입력을 받고 결과를 출력하는 main()
    """
    # 입력
    size = int(input())
    rain_map = []
    for _ in range(size):
        n_row = list(map(int, sys.stdin.readline().strip().split(" ")))
        rain_map.append(n_row)

    # 결과
    count = [1] # 비가 안오는 경우 안전지대는 1인경우를 생각하면 무조건 1은 나온다.
    for rain_rain_h in range(1, 101):
        count.append(count_map(rain_map, rain_rain_h))
    print(max(count))

if __name__ == "__main__":
    main()
