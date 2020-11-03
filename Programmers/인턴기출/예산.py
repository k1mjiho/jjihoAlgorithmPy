# 그리디 알고리즘인거같음 : 현재 상황에서 제일 좋은 방법을 찾기
# 최대한 많은 부서의 물품을 구매할 수 있도록 만들기 
# 신청한 금액만큼 모두 지원해줘야 함
# d : 부서별로 신청한 금액이 들어 있는 배열
# budget : 예산
# '최대' 몇 개의 부서에 물품을 지원할 수 있는가?

def solution(d, budget):
    answer = 0
    # 일단 금액이 작은순으로 배열을 sort
    d.sort()
    # 그 후 반복문으로 예산에서 신청금액 뺀다
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1

    return answer

print(solution([1,2,3,3], 8))

# sort() VS sorted()
array = [5,4,2,3,1]
print('original',array)
print('sorted',sorted(array))
print('sort', array.sort())
print('after',array)