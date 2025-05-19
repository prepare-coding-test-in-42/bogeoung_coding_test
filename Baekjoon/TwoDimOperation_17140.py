from collections import Counter

def input_func():
    r,c,k = map(int, input().split())

    input_array = []
    for _ in range(3):
        input_array.append(list(map(int, input().split())))
    
    return r-1,c-1,k,input_array



def r_operation(input_array):
    max_row = 0
    new_input_array = []
    for row in input_array:
        count = Counter(x for x in row if x != 0)
        sorted_count = sorted(count.items(), key = lambda x : [x[1], x[0]])
        
        new_row = []
        for num, count in sorted_count:
            new_row.extend([num, count])
        max_row = max(max_row, len(new_row))
        new_input_array.append(new_row)

    for row in new_input_array:
        row.extend([0] * (max_row - len(row)))
        if len(row) > 100:
            row = row[:100]
    return new_input_array

def c_operation(input_array):
    transposed = list(zip(*input_array))  # 열 단위로 처리
    new_cols = []
    max_col = 0

    for col in transposed:
        count = Counter(x for x in col if x != 0)
        sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]))  # 개수, 숫자 기준 정렬

        new_col = []
        for num, cnt in sorted_items:
            new_col.extend([num, cnt])

        max_col = max(max_col, len(new_col))
        new_cols.append(new_col)

    # 열 길이 맞추기 (0으로 패딩)
    for col in new_cols:
        col.extend([0] * (max_col - len(col)))
        if len(col) > 100:
            col = col[:100]

    # 열들을 다시 행 중심으로 전치
    result = [list(row) for row in zip(*new_cols)]
    return result
        
def main():
    r,c,k,input_array = input_func()
    answer = 0
    while True:
        if answer > 100:
            answer = -1
            break
        if len(input_array) > r and len(input_array[r]) > c and input_array[r][c] == k:
                break
        if len(input_array) >= len(input_array[0]): # R연산
            input_array = r_operation(input_array)
        else: # C연산
            input_array = c_operation(input_array)
        answer += 1

    print(answer)

if __name__ == "__main__":
    main()