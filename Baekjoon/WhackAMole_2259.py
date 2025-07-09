'''
1. T초에 벌판의 x,y 좌표에 두더지가 나타나게 된다.
2. T초에 정확히 해당 위치에 존재하면 두더지를 잡을 수 있다.
3. T초에 도착하는 것도 잡을 수 있는 것으로 간주한다.
4. 정은이는 1초에 S만큼 이동할 수 있다.
5. 정은이가 잡을 수 있는 최대 마리의 수는?
'''
import math

n, s = 0, 0


class Person:
    def __init__(self, s):
        self.x = 0
        self.y = 0
        self.s = s

    def move(self, x, y):
        self.x = x
        self.y = y

    def calc_time(self, dest_x, dest_y, start_x=None, start_y=None):
        start_x = self.x if start_x is None else self.x
        start_y = self.y if start_y is None else self.y

        distance_x = abs(start_x - dest_x)
        distance_y = abs(start_y - dest_y)
        total_distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return total_distance / self.s


def input_func():
    global n, s
    n, s = map(int, input().split())
    JeoungEun = Person(s)

    moles = []
    for _ in range(n):
        x, y, t = map(int, input().split())
        moles.append([t, x, y, False])

    moles.sort(key=lambda x: [x[0], x[1], x[2]])
    return JeoungEun, moles


def run(person, moles):
    cur_time = 0
    count_caught_mole = 0

    for i in range(n):
        cur_mole = moles[i]
        # 이미 잡은 두더지
        if cur_mole[3] is True:
            continue
        cur_mole_need_time = person.calc_time(cur_mole[1], cur_mole[2])
        # 가장 처음 나타나는 두더지를 잡을 수 있는 경우
        if cur_time + cur_mole_need_time <= cur_mole[0]:
            expect_time = cur_mole_need_time + cur_time
            expect_x, expect_y = cur_mole[1], cur_mole[2]
            # 이동 후 다음 두더지를 잡을 수 있는 경우
            if i + 1 < n:
                next_mole = moles[i + 1]
                if expect_time + person.calc_time(next_mole[1], next_mole[2], expect_x, expect_y) <= next_mole[0]:
                    cur_mole[3] = True
                    cur_time = cur_mole[0]
                    person.move(cur_mole[1], cur_mole[2])
                # 이동 후 다음 두더지를 잡을 수 없는 경우 -> 더 적게 움직이는 곳으로 이동
                elif expect_time <= person.calc_time(next_mole[1], next_mole[2]):
                    cur_mole[3] = True
                    cur_time = cur_mole[0]
                    person.move(cur_mole[1], cur_mole[2])
                else:
                    next_mole[3] = True
                    cur_time = next_mole[0]
                    person.move(next_mole[1], next_mole[2])
            count_caught_mole += 1
    return count_caught_mole


def main():
    person, moles = input_func()
    answer = run(person, moles)
    print(answer)


if __name__ == "__main__":
    main()
