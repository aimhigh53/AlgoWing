def solution(alist):
    def f(x):
        return float(x)

    slist = []
    n = len(alist)
    anslist = []

    for i in range(n):
        s = alist[i]
        hr, mn, sec = '', '', ''
        dur = ''
        for j in range(11, 13):
            hr += s[j]
        for j in range(14, 16):
            mn += s[j]
        for j in range(17, 23):
            sec += s[j]
        for j in range(24, len(s) - 1):
            dur += s[j]
        dur = f(dur)
        fin_time = f(hr) * 3600 + f(mn) * 60 + f(sec)
        cur_time = round(fin_time - dur + 0.001, 4)

        slist.append((cur_time, fin_time))
    slist.sort(key=lambda x: x[0])

    for i in range(n):
        ans1, ans2 = 1, 1
        st, end = slist[i][0], slist[i][1]
        for j in range(len(slist)):
            if (i == j): continue
            if (st <= slist[j][0] <= st + 0.9991 or st <= slist[j][1] <= st + 0.9991 or
                    (slist[j][0] <= st and slist[j][1] >= end)):
                ans1 += 1
            if (end <= slist[j][0] <= end + 0.9991 or end <= slist[j][1] <= end + 0.9991):
                ans2 += 1
        ans = max(ans1, ans2)
        anslist.append(ans)

    answer = max(anslist)
    return answer