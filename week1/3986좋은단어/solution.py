def main():
    n, m = map(int, input().split())
    a = set([input() for _ in range(n)])
    b = set([input() for _ in range(m)])
    answer = list(a & b)
    answer.sort()

    print(len(answer))
    for ans in answer:
        print(ans)

if __name__=='__main__':
    main()