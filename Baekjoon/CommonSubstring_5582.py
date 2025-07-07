def run(input1, input2):
    n, m = len(input1), len(input2)
    dp = [0] * (m+1)
    result = 0

    for i in range(1, n+1):
        prev = 0
        for j in range(1, m+1):
            temp = dp[j]
            if input1[i-1] == input2[j-1]:
                dp[j] = prev + 1
                result = max(result, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return result


def main():
    input1 = input()
    input2 = input()

    answer = run(input1, input2)
    print(answer)

if __name__ == "__main__":
    main()
