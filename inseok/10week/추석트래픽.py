
from datetime import timedelta,datetime


def compare(time, moment):
    start = time
    end = time + timedelta(milliseconds=999)

    if start >= moment[0] and start <= moment[1]:
        return True
    elif end >= moment[0] and end <= moment[1]:
        return True
    elif start <= moment[0] and end >= moment[1]:
        return True

    return False


def extractStartEnd(lines):
    timelist=[]
    for i in lines:
        times = i.split(' ')
        date = str(times[0]) + " " + str(times[1])

        ###여기를 처리하지 못했었음
        if '.' in times[2]:
            delay = times[2].split('.')
            delay[1] = delay[1][0:-1]
        else:
            delay = list(times[2][0:-1])
            delay += ["0"]
            
        end=datetime.fromisoformat(date)
        start=end-timedelta(seconds=int(delay[0]),milliseconds=int(delay[1])-1)

        timelist.append([start,end])

    return timelist


def solution(lines):

    timelist=extractStartEnd(lines)

    answers = []
    for times in timelist:
        for time in times:
            answer = 0
            for moment in timelist:
                if compare(time, moment) == True:
                    answer += 1
            answers.append(answer)

    return max(answers)

############################



"""
def solution(lines):
    logs = []
    for line in lines:
        _, done, time = line.split()
        h, m, s = done.split(':')
        end = (int(h)*60*60 + int(m)*60 + float(s))*1000
        logs.append((end-float(time[:-1])*1000+1, end))

    length = len(logs)
    max_ = 1
    for i in range(length-1):
        cnt = 1
        for j in range(i+1, length):
            if logs[j][1] - logs[i][1] >= 4000:
                break
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        max_ = max(max_, cnt)
    return max_
"""
