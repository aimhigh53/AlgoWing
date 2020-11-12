import datetime

def solution(lines):
    answer = 0
    times = []
    for i in lines:
        temp = i.split()
        et, dur = ''.join(temp[0] + "T"+ temp[1]), float(temp[2].replace("s",""))
        end_time = datetime.datetime.fromisoformat(et)

        dur = datetime.timedelta(seconds= dur)

        times.append([end_time - dur + datetime.timedelta(seconds=0.001),end_time])

    print(times)
    sec = datetime.timedelta(seconds= 1)

    for time in times:

        for t in time:
            result = 0
            for st, et in times:
                if t <= et < t + sec or t <= st < t + sec:
                    result +=1
                elif st <= t and et >= t +sec:
                    result += 1

            answer = max(result, answer)

    return answer

solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])