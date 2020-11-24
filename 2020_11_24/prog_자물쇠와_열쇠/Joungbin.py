from copy import deepcopy

def solution(key, lock):
    n = len(lock)
    m = len(key)

    def rotate(key):
        rot_list = [[0] * m for _ in range(m)]
        for j in range(m):
            for i in range(m):
                rot_list[j][m - 1 - i] = key[i][j]
        return rot_list

    def istrue(x, y, list_check):
        cnt = 0
        for i in range(x, x + n):
            for j in range(y, y + n):
                if (list_check[i][j] != 1): break
                cnt += 1
        if (cnt == n ** 2): return True
        return False

    ans = False
    k = n + 2 * (m - 1)
    mp = [[0]*k for _ in range(k)]
    for i in range(n):
        for j in range(n):
            mp[i+m-1][j+m-1] = lock[i][j]

    for cases in range(4): # 4가지 Cases
        for i in range(n+m-1): # key가 움직이는 길이가 n+m-1
            for j in range(n+m-1):
                cur_sta=deepcopy(mp) # Current Status
                for i1 in range(m): # key 리스트와 cur_sta 리스트를 합침
                    for j1 in range(m):
                        cur_sta[i+i1][j+j1] = mp[i+i1][j+j1]+key[i1][j1]
                if(istrue(m-1, m-1, cur_sta)): ans = True
        key = rotate(key)

    return ans
