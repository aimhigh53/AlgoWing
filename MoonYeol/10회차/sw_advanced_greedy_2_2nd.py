def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l][1] < arr[h][1]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

def solution(freight, time):
    count = 0
    merge_sort(freight)
    #sort_fre = sorted(freight, key=lambda x: x[1])
    for i in freight:
        if time <= i[0]:
            time = i[1]
            count += 1
    return count


if __name__ == "__main__":
    T = int(input())
    freights = []
    for i in range(T):
        N = int(input())
        freight = []
        for j in range(N):
            freight.append(list(map(int, input().split())))
        freights.append(freight)

    for idx, value in enumerate(freights):
        answer = solution(value, 0)
        print("#" + str(idx + 1) + " " + str(answer))
