'''
지금 solution1 에서 시간 초과나옴
반복문 돌릴때마다 sort 돌리니까 시간 복잡도가 O(N^no)가 되었다
최대힙을 사용하자
'''

def solution(no, works):
    while no > 0:
        works.sort()

        if works[-1] == 0 or no == 0:
            break
        else:
            works[-1] -= 1
            no -= 1

    return sum([i ** 2 for i in works])