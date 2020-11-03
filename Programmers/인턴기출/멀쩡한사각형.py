# 일단 모든 정사각형의 갯수는 w*h
# 잘리는 사각형들의 규칙을 알아내자
# 최대공약수가 반복되는거같음

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(w,h):
    answer = 1
    answer = w*h - (w+h - gcd(w,h))

    return answer

print(solution(4,4))