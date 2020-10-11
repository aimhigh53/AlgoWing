def solution(people, limit):
    people.sort(reverse=True)
    wsum = 0
    idx = 0
    idx_right = len(people) - 1
    ans = 0
    while(idx <= idx_right):
        wsum += people[idx]
        idx += 1
        if(idx > idx_right):
            ans += 1
            break
        while(wsum + people[idx_right] <= limit):
            wsum += people[idx_right]
            idx_right -= 1
        ans += 1
        wsum = 0

    return ans