# 성적마다 성적 가중치 grades, 그리고 과목별 고유 가중치를 의미하는 weights
# 그리고 졸업학점 threshold있음
# grades * weights - threshold 구하기

def solution(grades, weights, threshold):
    answer = -1234567890
    summ = 0
    # 일단 grades 배열에 그 맞는거를 알려주자 - 하드코딩 ㄱㅊ은가
    dic = {'A+': 10, 'A0': 9, 'B+': 8, 'B0': 7, 'C+': 6,'C0': 5, 'D+': 4, 'D0': 3, 'F': 0}
    # print(dic['A+']) 이렇게 딕셔너리 함수 사용해서
    # 그리고 이거랑 weights함수 곱해서 합 찾기
    for i in range(len(grades)):
        summ += dic[grades[i]] * weights[i]

    answer = summ - threshold
    return answer

print(solution(["A+","D+","F","C0"], [2,5,10,3], 50))