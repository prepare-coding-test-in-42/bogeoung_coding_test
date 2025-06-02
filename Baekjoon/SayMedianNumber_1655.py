from sortedcontainers import SortedList

def input_func():
    n = int(input())

    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    return n, numbers

def calc_median_index(numbers):
    if len(numbers) % 2 == 0: # 중간에 있는 두 수중 작은 숫자
        return len(numbers) // 2 - 1
    else:
        return len(numbers) // 2

def main():
    n, numbers = input_func()
    cur_numbers = SortedList()
    for i in range(n):
        cur_numbers.append(numbers[i])
        # print(i, cur_numbers)
        print(cur_numbers[calc_median_index(cur_numbers)])

if __name__ == "__main__":
    main()