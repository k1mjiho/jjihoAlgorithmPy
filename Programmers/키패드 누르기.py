'''
if문 잘 쓰기
그리고 2,5,8,0일때 길이 계산 어떻게 하느냐
abs() 절대값 라이브러리 함수
'''

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
def solution(numbers, hand):
    answer = ''
    dic = {1: (0, 0), 2: (0, 1), 3: (0, 2)
        , 4: (1, 0), 5: (1, 1), 6: (1, 2)
        , 7: (2, 0), 8: (2, 1), 9: (2, 2)
        , '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    prev_R = '*'
    prev_L = '#'

    for num in numbers:
        if (num in [3, 6, 9]):
            answer += 'R'
            prev_R = num
        elif (num in [1, 4, 7]):
            answer += 'L'
            prev_L = num
        else:
            ld = abs(dic[num][0] - dic[prev_L][0]) + abs(dic[num][1] - dic[prev_L][1])
            rd = abs(dic[num][0] - dic[prev_R][0]) + abs(dic[num][1] - dic[prev_R][1])

            if (ld > rd):
                answer += 'R'
                prev_R = num
            elif (ld < rd):
                answer += 'L'
                prev_L = num
            else:
                if (hand == 'right'):
                    answer += 'R'
                    prev_R = num
                else:
                    answer += 'L'
                    prev_L = num
    return answer

print(solution(numbers, hand))