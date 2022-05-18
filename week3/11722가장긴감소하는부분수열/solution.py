import sys


def main():
	input_len:int = int(input())
	dp:list = [1 for _ in range(input_len)]
	arr:list =  list(map(int, sys.stdin.readline().strip().split(" ")))
	for i, i_val in enumerate(arr):
		for j ,j_val in enumerate(arr[:i]):
			if i_val < j_val:
				dp[i] =max(dp[i], dp[j] + 1)
	print(max(dp))

if __name__ == "__main__":
	main()
