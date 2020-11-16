def solution(s):
    lenS = len(s)
    minLen = lenS
    for length in range(1, lenS // 2 + 1):
        newS = [s[i:i + length] for i in range(0, len(s), length)]
        tempS = ''
        count = 1

        for pivot in range(len(newS) - 1):
            if newS[pivot] == newS[pivot + 1]:
                count += 1
            else:
                if count == 1:
                    tempS += newS[pivot]
                else:
                    tempS += str(count)
                    tempS += newS[pivot]
                    count = 1

        if count == 1:
            tempS += newS[-1]
        else:
            tempS += str(count)
            tempS += newS[-1]

        if minLen > len(tempS):
            minLen = len(tempS)

    answer = minLen
    return answer