from collections import deque

n = 0


def input_func():
    global n
    n, q = map(int, input().split())
    usado = [[] for _ in range(n)]

    for _ in range(n - 1):
        input_p, input_q, input_r = map(int, input().split())
        usado[input_p - 1].append((input_q - 1, input_r))
        usado[input_q - 1].append((input_p - 1, input_r))

    questions = []
    for _ in range(q):
        questions.append(list(map(int, input().split())))
    return usado, questions


def dfs(start, min_usado, visited, usado):
    count = 0
    stack = deque()
    stack.append(start)
    while stack:
        cur_node = stack.popleft()
        for next_node, cur_usado in usado[cur_node]:
            if not visited[next_node] and cur_usado >= min_usado:
                visited[next_node] = True
                count += 1
                stack.append(next_node)
    return count


def main():
    usado, questions = input_func()
    for k, v in questions:
        visited = [False] * n
        visited[v - 1] = True
        result = dfs(v - 1, k, visited, usado)
        print(result)


if __name__ == "__main__":
    main()
