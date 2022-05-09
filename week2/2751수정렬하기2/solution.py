import sys
# import time
# start_time = time.time()
# 예제 기준 time: 2.5560574531555176

n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for num in num_list:
    print(num)

# end_time = time.time()
# print("time:", end_time - start_time)
