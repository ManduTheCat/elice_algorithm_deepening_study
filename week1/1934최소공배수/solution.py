def gcd(arr):
    while arr[1]>0:
        arr[0], arr[1] = arr[1], arr[0]%arr[1]
    return arr[0]

def lcm(arr):
    return arr[0]*arr[1] // gcd(arr)

test_case = [list(map(int, input().split())) for _ in range(int(input()))]

for case in test_case:
    print(lcm(case))