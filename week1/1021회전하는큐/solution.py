def check(num):
    num_str = num if isinstance(num, str) else str(num)

    if len(num_str) < 2:
        num_str = '0' + num_str

    return num_str

def cal(num_str):
    num_str = check(num_str)
    temp_str = check(sum(list(map(int, num_str))))
    return num_str[-1] + temp_str[-1]

N = int(input())
count = 0
init = check(N)
prev = N

while True:
    count+=1
    curr = cal(prev)
    if count==1 and N==0:
        break
    if curr == init:
        break
    prev = curr

print(count)