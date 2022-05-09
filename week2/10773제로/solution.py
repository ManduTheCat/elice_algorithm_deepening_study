import sys
def main():
	count_input = int(input())
	stack = []
	for i in range(count_input):
		input_num = int( sys.stdin.readline().strip())
		if not input_num == 0:
			stack.append(input_num)
		else:
			stack.pop()
	print(sum(stack))

if __name__ == "__main__":
	main()
