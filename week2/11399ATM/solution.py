def main():
    N = int(input())
    times = list(map(int, input().split()))
    times.sort()

    waitings = [0] * len(times)

    for i, time in enumerate(times):
        if i==0:
            waitings[i] += time
            continue
        waitings[i] += (waitings[i-1] + time)
    
    print(sum(waitings))



if __name__=='__main__':
    main()