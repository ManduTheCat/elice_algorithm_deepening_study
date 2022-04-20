from fractions import Fraction
import sys
def recursive(num,i,lists, coef):
	if i == coef -1 :
		return lists[-1]
	i+=1
	return num + Fraction(1, recursive(lists[i],i,lists,coef))
def main():
	coef = int(input())
	inputs = list(map(int,sys.stdin.readline().strip().split()))
	print(recursive(inputs[0], 0, inputs, coef))


if __name__ =="__main__":
	main()
