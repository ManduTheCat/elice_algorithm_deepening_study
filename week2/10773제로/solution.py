k = int(input())
num_list = []

for i in range(k):
    n = int(input())
    if n == 0:
        num_list.pop()
    else:
        num_list.append(n)

print(sum(num_list))