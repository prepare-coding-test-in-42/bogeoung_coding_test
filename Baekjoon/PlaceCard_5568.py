from itertools import permutations

def input_func():
    n = int(input())
    k = int(input())

    numbers = [input() for _ in range(n)]

    return k, numbers

def make_added_numbers(numbers, k):
    perms = permutations(numbers, k)

    addedNumbers = set()

    for perm in perms:
        addedNumbers.add(int(''.join(perm)))

    return len(addedNumbers)

def main():
    k, input_numbers = input_func()
    answer = make_added_numbers(input_numbers,k)
    print(answer)

if __name__ == "__main__":
    main()

