from itertools import combinations

def input_func():
    n = int(input())

    ingredients = [ list(map(int, input().split())) for _ in range(n)]

    return ingredients

def run(ingredients):
    n = len(ingredients)
    min_diff = 1000000000

    for num_ingredients in range(n, 0, -1):
        combs = combinations(ingredients, num_ingredients)

        for comb in combs:
            added_sour = 1
            added_bitter = 0
            for sour, bitter in comb:
                added_sour *= sour
                added_bitter += bitter
            min_diff = min(min_diff, abs(added_sour - added_bitter))

    return min_diff

def main():
    ingredients = input_func()
    answer = run(ingredients)
    print(answer)

if __name__ == "__main__":
    main()