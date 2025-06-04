import copy
from itertools import permutations


def input_func():
    n = int(input())

    potion_prices = list(map(int, input().split()))
    discount_prices = []
    for i in range(n):
        current_potion_discounts = []
        current_potion_discount_counts = int(input())
        for _ in range(current_potion_discount_counts):
            current_potion_discounts.append(list(map(int, input().split())))
        discount_prices.append(current_potion_discounts)

    return potion_prices, discount_prices


def potion_prices_update(potion_prices, discount_prices):
    potion_prices_copy = potion_prices[:]

    for potion_index, potion_price in discount_prices:
        potion_prices_copy[potion_index - 1] -= potion_price
        if potion_prices_copy[potion_index - 1] <= 0:
            potion_prices_copy[potion_index - 1] = 1

    return potion_prices_copy


def run(potion_prices, discount_prices):
    answer = 1000000
    potion_indices = [int(i) for i in range(len(potion_prices))]
    perms = permutations(potion_indices, len(potion_prices))

    for perm in perms:
        current_prices = 0
        current_potion_prices = potion_prices[:]
        for potion_index in perm:
            current_prices += current_potion_prices[potion_index]
            if discount_prices[potion_index]:
                current_potion_prices = potion_prices_update(current_potion_prices, discount_prices[potion_index])

        answer = min(answer, current_prices)
    return answer


def main():
    potion_prices, discount_prices = input_func()
    answer = run(potion_prices, discount_prices)
    print(answer)


if __name__ == "__main__":
    main()
