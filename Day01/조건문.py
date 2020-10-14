# 프로그램의 흐름을 제어하는 문법
# 코드의 블록을 들여쓰기로 지정
a = -100
if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a > -10")
else:
    print("-10 > a")

# 성적 구간에 따른 학점 출력 예제
score = int(input())

if score < 70:
    print("C")
elif score < 85:
    print("B")
else:
    print("A")

# 논리연산자는 직관적임
# or And not
if True or False:
    print("Yes")

# pass 키워드 : 아무것도 처리하고 싶지않을 때 사용 (그냥 비워두면 에러)