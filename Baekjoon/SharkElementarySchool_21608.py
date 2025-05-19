from collections import OrderedDict

near_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n = 0


def input_func():
    global n
    n = int(input())

    students = OrderedDict()
    for i in range(n * n):
        student_num, fav1, fav2, fav3, fav4 = map(int, input().split())
        students[student_num] = [fav1, fav2, fav3, fav4]

    return students


def count_fav(i, j, school, fav_students):
    fav_count = 0
    for mx, my in near_directions:
        nx, ny = i + mx, j + my
        if 0 <= nx < n and 0 <= ny < n and school[nx][ny] in fav_students:
            fav_count += 1
    return fav_count


def count_empty_space(row, col, school):
    count = 0

    for dx, dy in near_directions:
        nx, ny = row + dx, col + dy
        if 0 <= nx < n and 0 <= ny < n and school[nx][ny] == 0:
            count += 1
    return count


def find_loc(student_fav, school):
    candidate_locs = []
    for i in range(n):
        for j in range(n):
            if school[i][j] == 0:
                fav_count = count_fav(i, j, school, student_fav)
                empty_count = count_empty_space(i, j, school)
                candidate_locs.append([i, j, fav_count, empty_count])

    candidate_locs.sort(key=lambda x: [-x[2], -x[3], x[0], x[1]])
    return candidate_locs[0][0], candidate_locs[0][1]


def main():
    students = input_func()
    answer = 0
    school = [[0 for _ in range(n)] for _ in range(n)]

    for student, student_fav in students.items():
        selected_row, selected_col = find_loc(student_fav, school)
        school[selected_row][selected_col] = student

    for i in range(n):
        for j in range(n):
            current_student_num = school[i][j]
            fav_count = count_fav(i,j,school, students[current_student_num])
            if fav_count > 0:
                answer += 10 ** (fav_count - 1)

    print(int(answer))


if __name__ == "__main__":
    main()
