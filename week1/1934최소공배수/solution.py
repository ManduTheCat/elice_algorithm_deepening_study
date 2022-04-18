import sys
import math
def main():
	input_count = int(input())
	input_data_list = []
	for _ in range(input_count):
		input_data_list.append(list(map(int, sys.stdin.readline().strip().split(" "))))

	for input_list in input_data_list:
		a = input_list[0]
		b = input_list[1]
		print(a * b // math.gcd(a,b))

if __name__== "__main__":
	main()
