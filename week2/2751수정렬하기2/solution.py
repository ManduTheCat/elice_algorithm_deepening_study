import sys

def main():
	input_count = int(input())
	num_list = []
	for _ in range(input_count):
		input_num = int(sys.stdin.readline().strip())
		num_list.append(input_num)
	num_list.sort()
	for num in num_list:
		print(num)


if __name__ == "__main__":
	main()
