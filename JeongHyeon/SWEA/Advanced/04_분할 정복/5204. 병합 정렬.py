## 5204. 병합 정렬
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def merge(list):
    cnt = 0
    if len(list) <= 1:
        return list, cnt
    else:
        # 1개 될 때까지 계속 분리
        left, left_cnt = merge(list[:len(list)//2])
        right, right_cnt = merge(list[len(list)//2:])

        # 리스트 병합
        final_list = [] # 리턴 할 리스트
        left_idx = right_idx = 0 # 좌우측 인덱스
        last_small = '' # 마지막 원소 크기 비교

        for _ in range(len(list)):

            # left 종료
            if left_idx == len(left):
                final_list.append(right[right_idx])
                right_idx += 1
                last_small = 'left'

            # right 종료
            elif right_idx == len(right):
                final_list.append(left[left_idx])
                left_idx += 1
                last_small = 'right'

            # left가 작을 때
            elif left[left_idx] <= right[right_idx]:
                final_list.append(left[left_idx])
                left_idx += 1

            # right가 작을 때
            elif right[right_idx] < left[left_idx]:
                final_list.append(right[right_idx])
                right_idx += 1

        # cnt 계산
        cnt = left_cnt + right_cnt
        if last_small == 'right':
            cnt += 1

        return final_list, cnt

def sorted_merge(list):
    sorted_list, cnt = merge(list)
    return sorted_list[N//2], cnt

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    print(sorted_merge(L)) # (2, 0)
    print('#' + str(test_case), *sorted_merge(L)) # *sorted_merge(L) ???