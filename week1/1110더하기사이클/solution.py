num = int(input())
check = num
temp = 0
count = 0
new_num = 0

while True:
    temp = (num//10) + (num%10)
    new_num =(num%10)*10 + temp%10
    count += 1
    num = new_num
    if num == check:
        break

print(count)
