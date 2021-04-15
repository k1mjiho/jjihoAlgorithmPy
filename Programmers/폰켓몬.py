'''
처음에는 조합을 생각하고 풀었는데
solution1은 시간초과로 4문제 통과 못했다
조합을 하나하나 하면 시간이 너무 오래걸린다 -> 굳이 조합을 할 필요가 있는가?
생각1 중복제거한 len(set(nums)) < len(nums) / 2 라면 그냥 len(set(nums))를 리턴하면 되는거였다
생각2 그렇지않다면? 그냥 len(nums) / 2를 리턴하면 됨
'''
import itertools

def solution1(nums):
    answer = 0

    half = int(len(nums) / 2)
    nums = list(set(nums))
    len_S = len(nums)

    result = list(itertools.combinations(nums, half))

    if (len_S >= half):
        answer = len(result[0])
    else:
        answer = len_S

    return answer


def solution2(nums):
    answer = len(set(nums))
    half = len(nums) / 2

    if(answer > half):
        answer = half

    return answer

# 검색해보니 바로 리턴할 수 있는 답이 있었다.
def solution3(nums):
    return len(set(nums)) if len(set(nums)) < len(nums) / 2 else len(nums) / 2