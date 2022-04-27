import sys

def main():
	n, m = map(int, sys.stdin.readline().strip().split(" "))
	n_list = set()
	m_list = set()
	for _ in range(n):
		n_list.add(str(sys.stdin.readline().strip()))
	for _ in range(m):
		m_list.add(str(sys.stdin.readline().strip()))
	res = list(n_list & m_list)
	res.sort()
	print(len(res))
	for el in res:
		print(el)
if __name__ == "__main__":
	main()
