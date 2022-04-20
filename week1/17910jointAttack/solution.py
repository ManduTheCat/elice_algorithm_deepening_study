from fractions import Fraction

def add(left, right):
    x_list.pop()
    # print("pop된 x_list:", x_list)
    if len(x_list) == 1:
        left = x_list[-1]
        right = Fraction(1, right)
        # print("1left:", left, "1right:", right)
        return Fraction(left + right)
    else:
        # print("2left:", left, "2right:", right)
        # print("next left:", x_list[-2], "next right:", Fraction(left + Fraction(1, right)))
        return add(x_list[-2], left + Fraction(1, right))

x = int(input())
x_list = list(map(int, input().split()))
if len(x_list) == 1:
    print(x_list[0])
else:
    print(add(x_list[-2], x_list[-1]))