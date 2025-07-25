import math


def is_power_of(n, input_num):
    if input_num <= 1:
        return [False, -1]

    exponent = 0
    while n ** exponent <= input_num:
        if n ** exponent == input_num:
            return [True, exponent]
        else:
            exponent += 1
    return [False, -1]


def dp(m):
    is_power, exponent = is_power_of(2, m)
    if is_power:
        return 3 * (2 ** (exponent - 1))

    is_power, exponent = is_power_of(5, m)
    if is_power:
        return 4 * (5 ** exponent)

    is_power, exponent = is_power_of(5, m / 2)
    if is_power:
        return 12 * (5 ** exponent)

    prev, cur = 1,1
    pisano_len = 1

    for i in range(3, m**2 + 1):
        prev, cur = cur, (prev + cur) % m
        pisano_len += 1
        if prev == 0 and cur == 1:
            return pisano_len
    return None

def main():
    p = int(input())

    for i in range(p):
        n, m = map(int, input().split())
        print(n, dp(m))


if __name__ == "__main__":
    main()
