import itertools

def solution(nums):
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

    return len(set(nums)) if len(nums) // 2 > len(set(nums)) else len(nums) // 2