'''
zfill 원하는 길이가 안될때 앞에 0을 붙여준다
아 맞다 파이썬에서는 &&이런거 안쓰고 and or을 썼었지!!!
'''

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):

        t1 = format(arr1[i], 'b').zfill(n)
        t2 = format(arr2[i], 'b').zfill(n)
        str = ''

        for j in range(n):
            if (t1[j: j + 1] == '0' and t2[j:j + 1] == '0'):
                str += ' '
            elif (t1[j: j + 1] == '1' or t2[j:j + 1] == '1'):
                str += '#'

        answer.append(str)

    return answer