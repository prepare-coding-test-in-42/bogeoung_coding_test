from collections import defaultdict
def solution(genres, plays):
    answer = []
    playDict = defaultdict(list)

    for idx, genre in enumerate(genres):
        playDict[genre].append([idx, plays[idx]])

    totalPlays = []
    for genre, playTimes in playDict.items():
        playTimes.sort(key=lambda x: [-x[1], x[0]])
        playTimeSum = 0
        for playTime in playTimes:
            playTimeSum += playTime[1]
        totalPlays.append([genre, playTimeSum])

    totalPlays.sort(key=lambda x: -x[1])
    for sortedGenre in totalPlays:
        sortedGenrePlays = playDict[sortedGenre[0]]
        for i in range(min(2, len(sortedGenrePlays))):
            answer.append(sortedGenrePlays[i][0])
    return answer
