'''
지금 solution1 에서 시간 초과나옴
반복문 돌릴때마다 sort 돌리니까 시간 복잡도가 O(N^no)가 되었다
최대힙:시간 복잡도 O(logN) 을 사용하자

힙정렬은 최소힙밖에 없으므로
- 를 붙여서 다시 최대힙으로 바꿔준다음에
최대값을 찾는다
'''

def solution1(no, works):
    while no > 0:
        works.sort()

        if works[-1] == 0 or no == 0:
            break
        else:
            works[-1] -= 1
            no -= 1

    return sum([i ** 2 for i in works])


import heapq
def solution2(no, works):
    if no > sum(works):
        return 0
    else:
        works = [(-i, i) for i in works]
        heapq.heapify(works)

        for _ in range(no):
            work = heapq.heappop(works)[1] - 1

            heapq.heappush(works, (-work, work))

        return sum(i[1] ** 2 for i in works)

