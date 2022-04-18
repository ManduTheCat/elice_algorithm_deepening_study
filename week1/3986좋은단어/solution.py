import sys
def main():
	input_count = int(input())
	ans = 0
	input_word = [list(sys.stdin.readline().strip()) for _ in range(input_count)]
	for word in input_word:
		stack = []
		for ch in word:
			if not stack:
				stack.append(ch)
			elif stack[-1] == ch:
				stack.pop()
			elif stack[-1] != ch:
				stack.append(ch)
		if not stack:
			ans+=1
	print(ans)
if __name__ == "__main__":
	main()
