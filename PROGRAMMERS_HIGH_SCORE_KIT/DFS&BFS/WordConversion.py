answer = 100


def count_diff_word(word1, word2):
    count = 0

    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
    return count


def dfs(cur_word, count, visited, words, target):
    global answer
    if cur_word == target:
        answer = min(answer, count)
        return

    for new_word in words:
        if count_diff_word(cur_word, new_word) == 1 and new_word not in visited:
            dfs(new_word, count + 1, visited + [new_word], words, target)


def solution(begin, target, words):
    global answer
    dfs(begin, 0, [begin], words, target)
    if target not in words:
        return 0

    return answer