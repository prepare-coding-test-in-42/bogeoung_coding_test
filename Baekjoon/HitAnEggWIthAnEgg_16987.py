from itertools import permutations
from copy import deepcopy

class Egg():
    def __init__(self, d, w, i):
        self.durability = d
        self.weight = w
        self.index = i
        self.is_cracked = False

    def crack_check(self):
        if self.durability <= 0:
            self.is_cracked = True
            return True
        return False


class Eggs():
    def __init__(self):
        self.eggs = []

    def add_egg(self, egg):
        self.eggs.append(egg)

    def get_other_eggs(self, cur_index):
        return [egg for egg in self.eggs if egg.index != cur_index and egg.crack_check() is False]

    def get_egg(self, finding_egg_index):
        for egg in self.eggs:
            if egg.index == finding_egg_index:
                return egg
        return None

    def egg_fight(self, egg1_index, egg2_index):
        egg1, egg2 = self.get_egg(egg1_index), self.get_egg(egg2_index)
        egg1.durability -= egg2.weight
        egg2.durability -= egg1.weight

        crack_count = 0
        if egg1.crack_check():
            crack_count += 1
        if egg2.crack_check():
            crack_count += 1
        return crack_count


n = 0


def input_func():
    global n
    n = int(input())

    eggs = Eggs()
    for i in range(n):
        d, w = map(int, input().split())
        eggs.add_egg(Egg(d, w, i))
    return eggs


def get_new_sequence_eggs(eggs, order):
    new_sequence_eggs = Eggs()
    for idx in order:
        new_sequence_eggs.add_egg(deepcopy(eggs.eggs[idx]))
    return new_sequence_eggs


def calc_broken_eggs(new_sequence_eggs):
    broken_egg_count = 0
    for i in range(n):
        cur_egg = new_sequence_eggs.eggs[i]
        other_eggs = new_sequence_eggs.get_other_eggs(cur_egg.index)
        for other_egg in other_eggs:
            if cur_egg.crack_check():
                break
            broken_egg_count += new_sequence_eggs.egg_fight(cur_egg.index, other_egg.index)

    return broken_egg_count


def run(default_eggs):
    max_broken_eggs = 0
    perms = permutations([i for i in range(n)], n)
    for perm in perms:
        new_sequence_eggs = get_new_sequence_eggs(default_eggs, perm)
        # temp = calc_broken_eggs(new_sequence_eggs)
        # max_broken_eggs = max(max_broken_eggs, temp)
        max_broken_eggs = max(max_broken_eggs, calc_broken_eggs(new_sequence_eggs))
        # print(perm, temp)
    return max_broken_eggs


def main():
    eggs = input_func()
    answer = run(eggs)
    print(answer)


if __name__ == "__main__":
    main()
