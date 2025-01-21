import heapq

def addJobs(jobs, heapJobs, curTime):
    maxIndex = -1
    for i in range(len(jobs)):
        jobArriveTime, jobTimeTaken = jobs[i][0], jobs[i][1]
        if jobArriveTime <= curTime:
            heapq.heappush(heapJobs, (jobTimeTaken, jobArriveTime))
            maxIndex = i
    if maxIndex >= 0:
        jobs = jobs[maxIndex + 1:]

    return jobs


def scheduling(heapJobs, curTime, answer, jobs):
    while heapJobs:
        # 가장 소요시간이 적은 것부터 추출
        curJobTimeTaken, curJobArriveTime = heapq.heappop(heapJobs)

        if curTime < curJobArriveTime:
            curTime = curJobArriveTime
        answer += ((curTime - curJobArriveTime) + curJobTimeTaken)
        curTime += curJobTimeTaken

        jobs = addJobs(jobs, heapJobs, curTime)

    return [curTime, answer, jobs]


def solution(jobs):
    answer = 0
    lenJobs = len(jobs)
    heapJobs = []
    heapq.heapify(heapJobs)
    curTime = 0
    jobs.sort(key=lambda x: [x[0], x[1]])
    while jobs:
        firstJob = jobs.pop(0)
        heapq.heappush(heapJobs, (firstJob[1], firstJob[0]))
        curTime, answer, jobs = scheduling(heapJobs, curTime, answer, jobs)

    return answer // lenJobs