from collections import Counter
def solution(nums):
    answer = 0

    counter = Counter(nums)
    halfSizeOfNums = len(nums) // 2

    if (halfSizeOfNums >= len(counter)):
        answer = len(counter)
    if (halfSizeOfNums < len(counter)):
        answer = halfSizeOfNums

    return answer
