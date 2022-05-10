"""
입력을 위한 sys
dfs queue 생성을 위한 deque
"""
import sys
from collections import deque

def bfs(filed, row, col):
    """
    입력 받은 좌표 bfs
    """
    que = deque()
    que.append([row, col])
    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]
    while que:
        cur_node = que.popleft()
        for dist_index, _ in enumerate(d_x):
            next_node = [cur_node[0] + d_x[dist_index], cur_node[1] + d_y[dist_index]]
            try:
                next_node_value = filed[next_node[0]][next_node[1]]
                if next_node_value is True and next_node[0] != -1 and next_node[1] != -1:
                    filed[next_node[0]][next_node[1]] = False
                    que.append([next_node[0], next_node[1]])
            except IndexError:
                continue

def counter(filed):
    """
    bfs 로 진입할때
    배추 그룹 count
    """
    count = 0
    for row, row_value in enumerate(filed):
        for col, bool_value in enumerate(row_value):
            if bool_value is True:
                count += 1
                bfs(filed, row, col)
    return count

def main():
    """
    밭 갯수에 맞춰 루프돌리고 배추 는 true 인 밭 만들고 count 함수로 보네기
    """
    field_count = int(input())
    for _ in range(field_count):
        col_len, row_len, cabbage_count = map(int, sys.stdin.readline().strip().split(" "))
        field = [[False for _c in range(col_len)] for _r in range(row_len)]
        for __ in range(cabbage_count):
            col, row = map(int, sys.stdin.readline().strip().split(" "))
            field[row][col] = True
        print(counter(field))

if __name__ == "__main__":
    main()
