def solution(name):
    count = 0
    N = len(name)

    for ch in name:
        min_up_down = min(ord(ch) - ord('A'), 26 + ord('A') - ord(ch))
        count += min_up_down

    move = N - 1
    for left in range(N):
        idx = left + 1
        while (idx < N) and (name[idx] == 'A'):
            idx += 1

        right = N - idx
        back_distance = min(left, right)
        move = min(move, left + right + back_distance)

    count += move
    return count