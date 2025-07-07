def input_func():
    n = int(input())

    m = int(input())
    fixed_seats = []
    for _ in range(m):
         fixed_seats.append(int(input()))

    return n, fixed_seats

def make_dp(n):
    dp = [0 for _ in range(n+2)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+2):
        dp[i] = dp[i-1] + dp[i-2]
    return dp


def main():
    n, fixed_seats = input_func()
    
    answer = 1
    start_index = 0
    dp_result = make_dp(n)

    for fixed_num in fixed_seats:
        answer *= dp_result[fixed_num - 1 - start_index]
        start_index = fixed_num

    remain_length = n - start_index
    answer *= dp_result[remain_length]

    print(answer)

if __name__ == "__main__":
    main()