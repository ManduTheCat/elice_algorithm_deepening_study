from sys import stdin

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack: # 스택이 빌 때까지
        n = stack.pop()
        if n not in visited: # 방문한 적 없으면
            visited.append(n)
            # print("인접 노드들:", graph[n])
            temp = list(set(graph[n]) - set(visited))
            temp.sort(reverse=True)
            stack += temp
            # print("stack:", stack)
    print(*visited)

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue: # 큐가 빌 때까지
        n = queue.pop(0)
        if n not in visited: # 방문한 적 없으면
            visited.append(n)
            near_list = list(set(graph[n]) - set(visited)) # 집합은 sort가 보장되지 않는다!!! 그러므로 인접노드들을 직접 sort 해줘야됨!! 이거 몰라서 1시간 잡아먹음!!
            # print("n:", n, ", 연결된 노드:", near_list)
            near_list.sort()
            queue += near_list
            # print("queue:", queue)
    print(*visited)

n, m, v = map(int, stdin.readline().split())

# graph = [[0] * (n + 1) for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]

# 인접 리스트 방식
for i in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

dfs(graph, v)
bfs(graph, v)

# 드디어 반례찾음;;
# 15 14 1
# 1 2
# 1 3
# 1 4
# 2 5
# 2 6
# 3 7
# 3 8
# 3 9
# 4 10
# 4 11
# 4 12
# 6 13
# 9 14
# 9 15
# ----
# 1 2 5 6 13 3 7 8 9 14 15 4 10 11 12 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 