def solution(arr):
    answer = []

    for num in arr:
        if [num] != answer[-1:]:
            answer.append(num)

    return answer