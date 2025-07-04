n = 0


def input_func():
    global n
    n = int(input())

    buildings_height = list(map(int, input().split()))

    return buildings_height


def get_func(i, j, buildings_height):
    i_height = buildings_height[i]
    j_height = buildings_height[j]

    alpha = (j_height - i_height) / (j - i)
    beta = i_height - ((i + 1) * alpha)
    return alpha, beta


def is_under_function(alpha, beta, x, real_y):
    expectation_y = alpha * (x + 1) + beta
    return expectation_y > real_y


def count_best_buildings(buildings_height):
    # 가장 많은 건물이 보이는 건물을 구함
    max_num_visible_buildings = 0

    for i in range(n):
        cur_visible_buildings = 0
        for j in range(n):
            if i == j:
                continue
            # i 빌딩과 j 빌딩을 지나는 함수 구하기
            alpha, beta = get_func(i, j, buildings_height)

            # 사이에 있는 모든 빌딩이 함수 아래에 있는지 확인
            flag = True
            if i + 1 <= j:
                for x in range(i + 1, j):
                    if not is_under_function(alpha, beta, x, buildings_height[x]):
                        flag = False
                        break
            else:
                for x in range(j + 1, i):
                    if not is_under_function(alpha, beta, x, buildings_height[x]):
                        flag = False
                        break

            # 모두 아래에 있다면 cur_visible_buildings += 1
            if flag:
                cur_visible_buildings += 1

        # print(f"{i}번째 건물에서 보이는 건물의 수는 {cur_visible_buildings}")
        max_num_visible_buildings = max(max_num_visible_buildings, cur_visible_buildings)

    return max_num_visible_buildings


def main():
    buildings_height = input_func()
    answer = count_best_buildings(buildings_height)
    print(answer)


if __name__ == "__main__":
    main()
