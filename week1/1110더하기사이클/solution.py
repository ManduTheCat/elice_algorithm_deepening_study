
def main():
	n = str(input())
	#주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의
	# 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
	if int(n) < 10:
		n = str(10 * int(n))
	count = 1
	nextNum = n[-1] + str(int(n[0])+ int(n[-1]))
	# while(nextNum != n)에서 int 로 변환하니 시간 초과 해결 왜?
	while(int(nextNum) != int(n)):
		count+=1
		nextNum = str(nextNum[-1]) + str(int(nextNum[0])+int(nextNum[-1]))[-1]
		# 더한수는 자리수가 몇이든 마지막 자리가 반영된다
	print(count)
if __name__ =="__main__":
	main()
