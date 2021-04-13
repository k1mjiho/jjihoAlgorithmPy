'''
pass는 그냥 넘어가고 다음 코드를 계속 수행
continue는 다음 코드 넘어가고 다음 순번의 loop를 실행시킨다
정규식을 잘 활용하자
변수 idx 계산 잘하기
'''
import re  # 문자열 라이브러리
import math  # 수학함수 라이브러리

def solution2(dartResult):
    cnt = 0
    alpha = {'S': 1, 'D': 2, 'T': 3}
    # 문자열에서 숫자만 int형 으로 뽑아 리스트
    num = list(map(int, re.findall('\d+', dartResult)))
    strs = list(map(str, re.findall('\D', dartResult)))

    for idx, s in enumerate(strs):
        tmp = num[cnt]
        if s in alpha:
            num[cnt] = math.pow(tmp, alpha[s])
        elif (s == '#'):
            num[cnt] *= -1
        elif (s == '*'):
            num[cnt] *= 2
            if (cnt > 0):  # num[0]이 아니면 그 이전 숫자도 *2
                num[cnt - 1] = num[cnt - 1] * 2

        # 다음이 S,D,T중에 하나라면 num의 idx+1
        if (idx + 1 < len(strs) and strs[idx + 1].isalpha()):
            cnt += 1

    return sum(num)

def solution(dartResult):
    cnt = 0
    alpha = { 'S':1, 'D' : 2}
    # 문자열에서 숫자만 int형으로 뽑아 리스트
    num = list(map(int, re.findall('\d+', dartResult)))
    strs = list(map(str, re.findall('\D', dartResult)))

    for idx, s in enumerate(strs):
        tmp = num[cnt]

        if (s == 'S'):
            pass  # cnt+1 하는 if문은 타야하기때문에
        elif (s == 'D'):
            num[cnt] = math.pow(tmp, 2)
        elif (s == 'T'):
            num[cnt] = math.pow(tmp, 3)
        elif (s == '#'):
            num[cnt] *= -1
        elif (s == '*'):
            num[cnt] *= 2
            if (cnt > 0):  # num[0]이 아니면 그 이전 숫자도 *2
                num[cnt - 1] = num[cnt - 1] * 2

        # 다음이 S,D,T중에 하나라면 num의 idx+1
        if (idx + 1 < len(strs) and strs[idx + 1].isalpha()):
            cnt += 1

    return sum(num)