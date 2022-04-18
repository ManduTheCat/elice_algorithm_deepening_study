import sys
def main():
	input_count = int(input())
	input_bracket = [list(sys.stdin.readline().strip()) for _ in range(input_count)]

	for bracket_list in input_bracket:
		stack = []
		if bracket_list[0] == ")":
			print("NO")
			continue
		for bracket in bracket_list:
			if not stack:
				stack.append(bracket)
			elif stack[-1] == bracket:
				stack.append(bracket)
		#무조건 서로 다른게 아니라  ( 로 시작해서) 로 끝나야한다. 즉 시작하는 브라캣은 정해져있다.
			elif stack[-1] == "(" and bracket == ")":
				stack.pop()
		if not stack:
			# print(bracket_list)
			print("YES")
		elif stack:
			print("NO")

if __name__ == "__main__":
	main()
