from Baekjoon.SharkMiddleSchool_21609 import rotate_counter_clockwise


class Blocks:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def count_filled_block(self):
        return sum(row.count(1) for row in self.map)

    def add_block(self, blocks):
        move_x = 0
        while True:
            moved = [[r + move_x + 1, c] for r, c in blocks]
            if any(r >= self.row or self.map[r][c] != 0 for r, c in moved):
                break
            move_x += 1

        for r, c in blocks:
            self.map[r + move_x][c] = 1

    def check_rows(self):
        fullfilled_rows = []
        for row_index in range(self.row):
            if sum(self.map[row_index]) == self.col:
                fullfilled_rows.append(row_index)

        for index in fullfilled_rows:
            self.map.pop(index)
            self.map.append([0 for _ in range(self.col)])
        return len(fullfilled_rows)

    def check_light_row(self):
        for row_index in range(1, -1, -1):
            if 1 in self.map[row_index]:
                self.map.pop(row_index)  # 마지막 행 제거
                self.map.insert(0,[0 for _ in range(self.col)])  # 새로운 행 추가

    def count_filled_block(self):
        block_count = 0
        for row in self.map:
            block_count += row.count(1)
        return block_count


class Green(Blocks):
    def __init__(self):
        super().__init__(6,4)


class Blue(Blocks):
    def __init__(self):
        super().__init__(4,6)

    def rotate_clockwise(self):
        self.map =  [list(reversed(col)) for col in zip(*self.map)]

    def rotate_counter_clockwise(self):
        self.map = [list(row) for row in zip(*self.map)][::-1]

    def add_block(self, blocks):
        move_y = 0
        while True:
            moved = [[r, c + move_y + 1] for r, c in blocks]
            if any(c >= self.col or self.map[r][c] != 0 for r, c in moved):
                break
            move_y += 1

        for r, c in blocks:
            self.map[r][c+move_y] = 1

    def check_cols(self):
        self.rotate_clockwise()
        cols = super().check_rows()
        self.rotate_counter_clockwise()
        return cols

    def check_light_col(self):
        for col_index in range(1, -1, -1):
            for row_index in range(self.row):
                if self.map[row_index][col_index] == 1:
                    self.map[row_index].pop()  # 마지막 행 제거
                    self.map[row_index].insert(0,0)  # 새로운 행 추가

    def count_filled_block(self):
        self.rotate_clockwise()
        return super().count_filled_block()

def input_func():
    n = int(input())

    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().split())))

    return orders

def run(orders):
    block_types = [[[0,0]], [[0,0]], [[0,0], [0,1]], [[0,0], [1,0]]]
    blue_blocks = Blue()
    green_blocks = Green()
    score = 0
    for t,x,y in orders:
        added_blocks = []
        for direction in block_types[t]:
            new_x, new_y = x + direction[0], y + direction[1]
            added_blocks.append([new_x, new_y])

        green_blocks.add_block(added_blocks)
        blue_blocks.add_block(added_blocks)

        score += green_blocks.check_rows()
        score += blue_blocks.check_cols()
        print("-----Blue-----")
        for row in blue_blocks.map:
            print(row)
        print("-----Green-----")
        for row in green_blocks.map:
            print(row)
        print("================")

        green_blocks.check_light_row()
        blue_blocks.check_light_col()
    print("blue:", blue_blocks.count_filled_block())
    print("green:", green_blocks.count_filled_block())

    return [score, blue_blocks.count_filled_block() + green_blocks.count_filled_block()]

def main():
    orders = input_func()
    score, filled_block_count = run(orders)
    print(score)
    print(filled_block_count)


if __name__ == "__main__":
    main()
