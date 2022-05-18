import sys

def main():
    input_count = int(input())
    input_arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    dp = [i for i in input_arr]
    for anchor_index, anchor_val in enumerate(input_arr):
        for cursor_index , cursor_val in enumerate(input_arr[: anchor_index]):
            if anchor_val > cursor_val:
                dp[anchor_index] = max(dp[anchor_index], dp[cursor_index] + anchor_val)

    print(max(dp))
if __name__ == "__main__":
    main()
