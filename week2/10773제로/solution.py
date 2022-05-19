def main():
    N = int(input())
    stack = []

    for i in range(N):
        n = int(input())
        if (n==0):
            stack.pop()
            continue
        stack.append(n)
    
    print(sum(stack))

if __name__=='__main__':
    main()