def main():
	n = int(input())
	memo = [0,1]
	for i in range(n+1):
		memo.append(memo[i]+ memo[i+1])
	print(memo[n])

if __name__=="__main__":
	main()

