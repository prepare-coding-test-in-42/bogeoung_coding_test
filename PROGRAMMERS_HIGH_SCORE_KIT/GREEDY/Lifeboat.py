def solution(people, limit):
    answer = 0

    people.sort()

    left_idx = 0
    right_idx = len(people) - 1
    while left_idx <= right_idx:
        if people[left_idx] + people[right_idx] > limit:
            right_idx -= 1
        else:
            right_idx -= 1
            left_idx += 1
        answer += 1
    return answer


