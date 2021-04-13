import re
import math


def solution(dartResult):
    cnt = 0
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