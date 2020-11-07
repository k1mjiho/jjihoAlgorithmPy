def solution(s, op):
    answer = []
    global len
    len= len(s) #문자열 길이

    #받은 문자열 분리하기
    for i in range(len-1):

        s1 =int(''.join(map(str,s[0:i+1])))

        s2=int(''.join(map(str,s[i+1:len])))

        # 연산처리
        if(op=='+'):
            total=s1+s2
        elif(op=='-'):
            total=s1-s2
        else :
            total=s1 * s2

        answer.append(total)

    return answer

print(solution(1234,'+'))