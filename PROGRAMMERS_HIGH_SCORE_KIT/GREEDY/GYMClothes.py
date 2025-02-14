def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    for i in range(len(reserve)):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            reserve[i] = -1

    students = set()
    for i in range(1, n + 1):
        if i not in lost:
            students.add(i)

    for r_student in reserve:
        if r_student - 1 in lost:
            lost.remove(r_student - 1)
            students.add(r_student - 1)
        elif r_student + 1 in lost:
            lost.remove(r_student + 1)
            students.add(r_student + 1)

    return len(students)
