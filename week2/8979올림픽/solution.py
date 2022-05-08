def main():
    N, k = map(int, input().split())
    lines = [list(map(int, input.split())) for _ in range(N)]
    rank = 1
    k_line = [line for line in lines if line[0]==k].pop()
    gold_list = [line for line in lines if line[1]>k_line[1]]
    silver_list = [line for line in lines if line[1]==k_line[1] and line[2]>k_line[2]]
    bronze_list = [line for line in lines if line[1]==k_line[1] and line[2]==k_line[2] and line[3]>k_line[3]]

    rank += len(gold_list)
    rank += len(silver_list)
    rank += len(bronze_list)

    print(rank)

if __name__=='__main__':
    main()