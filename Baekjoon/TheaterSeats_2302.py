def input_func():
    n = int(input())

    m = int(input())
    fixed_seats = []
    for _ in range(m):
         fixed_seats.append(int(input()))

    return n, fixed_seats

def main():
    n, fixed_seats = input_func()

    start_index = 0
    for fixed_num in fixed_seats:
        end_index = fixed_num - 1


