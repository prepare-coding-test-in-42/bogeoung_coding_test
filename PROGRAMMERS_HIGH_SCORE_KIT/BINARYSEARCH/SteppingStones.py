def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance

    while left <= right:
        mid = (left + right) // 2
        delete_count = 0
        previous_rock = 0
        for rock in rocks:
            if rock - previous_rock < mid:
                delete_count += 1
                if delete_count > n:
                    break
            else:
                previous_rock = rock
        if delete_count > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer