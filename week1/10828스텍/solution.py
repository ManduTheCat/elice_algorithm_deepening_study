import sys
class Stack:
	def __init__ (self):
		self.storage = []
	def push(self, num):
		self.storage.append(num)
	def fpop(self):
		if self.storage:
			return self.storage.pop()
		else:
			return -1
	def top(self):
		if self.storage:
			return self.storage[-1]
		else:
			return -1
	def size(self):
		return len(self.storage)
	def empty(self):
		if self.storage:
			return 0
		else:
			return 1

def main():
	input_count = int(input())
	s = Stack()
	for _ in range(input_count):
		command = sys.stdin.readline().split()
		if command[0] == "push":
			s.push(command[1])
		elif command[0] == "pop":
			print(s.fpop())
		elif command[0] == "size":
			print(s.size())
		elif command[0] == "empty":
			print(s.empty())
		elif command[0] == "top":
			print(s.top())


if __name__ == "__main__":
	main()
