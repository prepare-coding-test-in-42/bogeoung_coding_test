def solution(A, B):
    answer = 0
    B.sort()

    for num in A:
        min_winning_index = find_winning_numbers(B, num)
        if min_winning_index > 0 or (min_winning_index == 0 and num < B[0]):
            answer += 1
            del B[min_winning_index]

    return answer


def find_winning_numbers(B, A_num):
    left = 0
    right = len(B) - 1
    min_winning_index = 0
    while left <= right:
        mid = (left + right) // 2
        if B[mid] > A_num:
            min_winning_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_winning_index