originalNumber = int(input())
count = 0
newNumber = originalNumber # 첫 시작 숫자가 입력숫자
# //10 십의 자리 , %10 일의 자리
while True:
    count += 1
    newNumber = (newNumber%10)*10+(newNumber//10+newNumber%10)%10
    if originalNumber == newNumber:
        break
print(count) 