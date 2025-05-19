TOP_IDX = 0
RIGHT_IDX = 2
BOTTOM_IDX = 4
LEFT_IDX = 6
NORTH = 0
SOUTH = 1
CLOCKWISE = 1
COUNTERCLOCKWISE = -1

import copy

# 1시간 소요
def input_func():
    cogwheels = []
    for i in range(4):
        temp = input()
        temp_list = []
        for char in temp:
            temp_list.append(int(char))
        cogwheels.append(Cogwheel(temp_list))

    k = int(input())
    commands = []
    for i in range(k):
        commands.append(list(map(int, input().split())))

    return cogwheels, commands


class Cogwheel:
    def __init__(self, numbers):
        self.numbers = numbers
        self.clockwise = True

    def rotate(self):
        temp_numbers = copy.deepcopy(self.numbers)
        if self.clockwise:  # 시계방향 회전
            temp_numbers.insert(0, temp_numbers.pop())
        else:  # 반시계방향 회전
            temp_numbers.append(temp_numbers.pop(0))
        return temp_numbers


def rotate_cogwheel(cogwheels, cur_wheel_idx, rotate_direction, is_right, is_left):
    if rotate_direction == 1:
        cogwheels[cur_wheel_idx].clockwise = True
    elif rotate_direction == -1:
        cogwheels[cur_wheel_idx].clockwise = False
    number_after_rotate = cogwheels[cur_wheel_idx].rotate()
    number_before_rotate = cogwheels[cur_wheel_idx].numbers

    # 오른쪽 바퀴 확인
    if is_right and cur_wheel_idx + 1 < 4:
        if cogwheels[cur_wheel_idx].numbers[RIGHT_IDX] != cogwheels[cur_wheel_idx + 1].numbers[LEFT_IDX]:
            cogwheels[cur_wheel_idx].numbers = number_after_rotate
            rotate_cogwheel(cogwheels, cur_wheel_idx + 1, rotate_direction * -1, 1, 0)
            cogwheels[cur_wheel_idx].numbers = number_before_rotate
    if is_left and cur_wheel_idx - 1 >= 0:
        if cogwheels[cur_wheel_idx].numbers[LEFT_IDX] != cogwheels[cur_wheel_idx - 1].numbers[RIGHT_IDX]:
            cogwheels[cur_wheel_idx].numbers = number_after_rotate
            rotate_cogwheel(cogwheels, cur_wheel_idx - 1, rotate_direction * -1, 0, 1)
            cogwheels[cur_wheel_idx].numbers = number_before_rotate
    cogwheels[cur_wheel_idx].numbers = number_after_rotate


def run(cogwheels, commands):
    for command in commands:
        move_wheel_idx, rotate_direction = command[0] - 1, command[1]
        rotate_cogwheel(cogwheels, move_wheel_idx, rotate_direction, 1, 1)

    answer = 0

    for idx, wheel in enumerate(cogwheels):
        # print(f"{idx}th wheel.numbers : {wheel.numbers}")
        if wheel.numbers[TOP_IDX] == SOUTH:
            answer += 2 ** idx
    print(answer)


def main():
    cogwheels, commands = input_func()
    run(cogwheels, commands)


if __name__ == "__main__":
    main()
