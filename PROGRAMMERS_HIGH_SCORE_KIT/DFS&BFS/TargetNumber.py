answer = 0

def dfs(numbers, index, target, cur_num):
    global answer
    if cur_num == target and index == len(numbers):
        answer += 1
        return
    if index > len(numbers) - 1:
        return
    if index <= len(numbers) - 1:
        dfs(numbers, index + 1, target, cur_num + numbers[index])
        dfs(numbers, index + 1, target, cur_num - numbers[index])

def solution(numbers, target):
    dfs(numbers, 0, target, 0)
    return answer
