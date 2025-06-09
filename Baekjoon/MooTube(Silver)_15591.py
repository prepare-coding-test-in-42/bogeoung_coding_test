'''
1. MOOTube에 1부터 N까지 번호가 붙여진 N개의 동영상이 존재.
2. 두 둉영상이 서로 얼마나 가까운지를 측정하는 단위 "USADO"
    2-1. 각 영상은 정점으로 나타냄
    2-2. 각 영상은 다른 영상으로 가는 경로가 반드시 하나는 존재
    2-3. 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최소값으로 함.
4. 값 K를 정해서, USADO가 K이상인 모든 동영상이 추천되고, K가 입력되었을 때의 추천될 영상의 개수를 구하기
'''
global n


def input_func():
    global n
    n, q = map(int, input().split())
    usado = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n - 1):
        input_p, input_q, input_r = map(int, input().split())
        usado[input_p - 1][input_q - 1] = input_r
        usado[input_q - 1][input_p - 1] = input_r

    questions = []
    for _ in range(q):
        questions.append(list(map(int, input().split())))
    return usado, questions


def get_minimum_usado(usado, i, j):
    for k in range(n):
        if usado[i][k] > 0 and usado[k][j] > 0:
            min_usado = min(usado[i][k], usado[k][j])
            usado[i][j] = min_usado
            usado[j][i] = min_usado


def update_usado(usado, row_index):
    # usado값이 정해지지 않은 값에 대해서 usado를 구함
    for j in range(n):
        if row_index == j:
            continue
        if usado[row_index][j] == 0:
            get_minimum_usado(usado, row_index, j)


def main():
    usado, questions = input_func()
    for k, v in questions:
        update_usado(usado, v)
        print(f"k: {k}, v : {v}")
        print(usado)
        cur_num_usado = usado[v - 1]
        print(sum(1 for num in cur_num_usado if num >= k))


if __name__ == "__main__":
    main()
