from math import ceil
def main():
	m = int(input())
	n = int(input())
	re = []
	for num in range(ceil(m**0.5),int((n**0.5)+1)):
		re.append(num**2)
	if(re):
		print(sum(re))
		print(min(re))
	else:
		print(-1)
if __name__ == "__main__":
	main()
