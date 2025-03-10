
def init_func():

    n = int(input())
    a = list(map(int, input().split()))
    b,c = map(int, input().split())

    return n,a,b,c

def main():
    n,a,b,c = init_func()
    answer = n

    for i in range(n):
        cur_examinee = a[i] - b
        if cur_examinee < 0:
            continue
        if cur_examinee % c != 0:
            answer += 1
        answer += cur_examinee // c

    print(answer)



if __name__ == "__main__":
    main()
