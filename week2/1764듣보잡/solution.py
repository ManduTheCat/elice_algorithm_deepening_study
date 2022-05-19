n_list, m_list = [], []
n, m = map(int, input().split())
for _ in range(n):
    n_list.append(input())
for _ in range(m):
    m_list.append(input())
result = list(set(n_list) & set(m_list))
result.sort()
print(len(result))
for person in result:
    print(person)
