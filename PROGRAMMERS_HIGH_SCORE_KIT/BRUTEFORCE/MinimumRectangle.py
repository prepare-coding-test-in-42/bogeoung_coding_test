def solution(sizes):
    w, h = [], []

    for num1, num2 in sizes:
        if num1 > num2:
            w.append(num1)
            h.append(num2)
        else:
            h.append(num1)
            w.append(num2)

    answer = max(w) * max(h)
    return answer