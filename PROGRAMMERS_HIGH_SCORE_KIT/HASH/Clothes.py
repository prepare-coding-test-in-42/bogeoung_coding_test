from collections import defaultdict
def solution(clothes):
    answer = 1
    clothDicts = defaultdict(list)

    for name, clothType in clothes:
        clothDicts[clothType].append(name)

    for key, value in clothDicts.items():
        answer *= (len(value) + 1)
    return answer - 1