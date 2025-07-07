from collections import deque
import sys

input = sys.stdin.readline


def d(n):
    return (2 * n) % 10000


def s(n):
    return 9999 if n == 0 else n - 1


def l(n):
    return (n % 1000) * 10 + (n // 1000)


def r(n):
    return (n % 10) * 1000 + (n // 10)


def run(a, b):
    visited = [False] * 10000
    prev = [-1] * 10000   # 이전 노드 저장
    how = [''] * 10000    # 이전 명령어 저장

    queue = deque()
    queue.append(a)
    visited[a] = True

    while queue:
        now = queue.popleft()
        if now == b:
            break
        for func, cmd in zip([d, s, l, r], "DSLR"):
            nxt = func(now)
            if not visited[nxt]:
                visited[nxt] = True
                prev[nxt] = now
                how[nxt] = cmd
                queue.append(nxt)

    # 경로 역추적
    result = []
    cur = b
    while cur != a:
        result.append(how[cur])
        cur = prev[cur]
    result.reverse()

    return ''.join(result)

def main():
    t = int(input())

    for i in range(t):
        a, b = map(int, input().split())
        answer = run(a, b)
        print(answer)


if __name__ == "__main__":
    main()
