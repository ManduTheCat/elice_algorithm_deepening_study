import sys
from collections import deque;
def main():
	numlang, iterator = map(int, sys.stdin.readline().strip().split())
	q = deque([_ for _ in range(1,numlang+1)])
	re = []
	while(q):
		for _ in range(iterator):
			q.append(q.popleft())
		re.append(q.pop())
	print("<", end="")
	print(*re, sep=", ", end="")
	print(">", end="")

if __name__ =="__main__":
	main()
