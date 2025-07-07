def run(input1, input2):
    longest_common_substring = 0
    start_index = 0
    for i in range(1, len(input1)): # 부분 문자열의 길이
        for j in range(start_index + len(input1) - i): # 부분 문자열의 시작점
            substring = input1[j: j+i]
            if substring in input2:
                longest_common_substring = i
                break
        if i != longest_common_substring:
            start_index = i + 1
    return longest_common_substring


def main():
    input1 = input()
    input2 = input()

    answer = 0

    if len(input1) < len(input2):
        answer = run(input1, input2)
    else:
        answer = run(input2, input1)
    print(answer)

if __name__ == "__main__":
    main()
