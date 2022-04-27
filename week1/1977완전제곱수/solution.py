import math

M = int(input())
N = int(input())
nums = []

for i in range(M, N + 1):
    if math.sqrt(i) == int(math.sqrt(i)):
        # print("correct:", math.sqrt(i), int(math. sqrt(i)))
        nums.append(i) # 완전제곱수를 리스트에 저장
    # print("incorrect:", math.sqrt(i), int(math.sqrt(i)))
if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)