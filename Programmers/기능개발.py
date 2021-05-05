'''
큐의 FIFO 속성을 잘 사용해보자
speeds에서 제일 왼쪽꺼 뽑는다 -> FIFO
'''
from collections import deque
def solution(pros, speeds):
    answer = []
    days = []
    speeds = deque(speeds)
    max_ = 0

    for pro in pros:
        day = 0
        basket = pro
        speed = speeds.popleft()

        while basket < 100:
            day += 1
            basket = pro + (day * speed)

        days.append(day)

    for i, work in enumerate(days):
        if i == 0:
            max_ = work
            answer.append(1)
            continue

        if max_ >= work:
            answer[-1] += 1
        else:
            max_ = work
            answer.append(1)

    return answer