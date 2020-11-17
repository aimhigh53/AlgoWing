def solution(s):
    LENGTH = len(s)
    lengths = [LENGTH]

    for size in range(1, LENGTH):
        compressed = ""
        splited = [s[i:i+size] for i in range(0, LENGTH, size)]
        count = 1
        pre = splited[0]
        for cur in splited[1:]:
            if pre == cur:
                count += 1
            else:
                compressed += (str(count) + pre) if count > 1 else pre
                count = 1
            pre = cur

        compressed += (str(count) + splited[-1]) if count > 1 else splited[-1]
        lengths.append(len(compressed))

    return min(lengths)  # 최솟값 리턴