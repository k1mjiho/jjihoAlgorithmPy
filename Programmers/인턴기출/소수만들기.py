# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수 구하기
# 이것도 그리디 알고리즘 같음
# 숫자들이 들어있는 배열 nums
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수 return
# 배열에 중복된 숫자 ㄴㄴ
# 이거 약간 순열조합 써야 될거같은디 -> n개중에 3개 골라서 이거 prime이냐 아니냐
# 조합 써야 함 : 순서를 생각하지않고 선택만 -> 순서가 바껴도 서로 같은것으로 취급하기때문
from itertools import combinations

def solution(nums):
    answer = 0
    array = []
    # 일단 nums 배열에서 임의로 3개 뽑음
    data = list(combinations(nums, 3))
    # 합계를 저장하는 배열 생성
    for i in range(len(data)):
        array.append(sum(data[i]))
    # 반복문 돌리면서 isPrime 확인
    for x in array:
        for i in range(2, x):
            if x % i == 0: # 약수 하나라도 있음 걍 break
                break
        else:
            answer += 1

    return answer

print(solution([1,2,3,4]))