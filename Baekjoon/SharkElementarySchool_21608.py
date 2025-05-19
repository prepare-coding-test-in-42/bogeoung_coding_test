from collections import OrderedDict
from collections import defaultdict

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


def calc_fav(i, j, school, fav_students):
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


def find_loc(student_fav, school, added_students):
    if len(added_students) > 0:
        count_only_location = defaultdict(int)
        for added_student, row, col in added_students:
            if added_student in student_fav:
                for direction in near_directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < n and 0 <= new_col < n and school[new_row][new_col] == 0:
                        count_only_location[(new_row, new_col)] += 1

        if len(count_only_location) > 0:
            calc_location = dict()
            for loc, count in count_only_location.items():
                calc_location[loc] = [count, count_empty_space(loc[0], loc[1], school)]
            sorted_calc_location = sorted(calc_location.items(), key=lambda x: [-x[1][0], -x[1][1], x[0][0], x[0][1]])
            return sorted_calc_location[0][0]

    candidate_loc = dict()
    for i in range(n):
        for j in range(n):
            if school[i][j] == 0:
                candidate_loc[(i, j)] = count_empty_space(i, j, school)

    sorted_candidate_loc = sorted(candidate_loc.items(), key=lambda x: [-x[1], x[0][0], x[0][1]])
    return sorted_candidate_loc[0][0]


def main():
    students = input_func()
    answer = 0
    school = [[0 for _ in range(n)] for _ in range(n)]

    added_students = []
    for student, student_fav in students.items():
        selected_row, selected_col = find_loc(student_fav, school, added_students)
        school[selected_row][selected_col] = student
        added_students.append([student, selected_row, selected_col])

    for i in range(n):
        for j in range(n):
            current_student_num = school[i][j]
            fav_count = calc_fav(i, j, school, students[current_student_num])
            if fav_count > 0:
                answer += 10 ** (fav_count - 1)

    print(int(answer))


if __name__ == "__main__":
    main()
