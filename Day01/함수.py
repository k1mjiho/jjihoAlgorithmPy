# def 함수명(매개변수):
#   실행할 소스코드
#   return 반환 값
def add(a,b):
    return a+b

print(add(3,4))

# 파라미터의 변수를 직접 지정 가능
def add(a,b):
    print("함수의 결과:", a+b)
# 순서 상관ㄴㄴ
add(b = 5, a =7)

# global 키워드 : 함수 바깥에 선언된 변수 참조하려고
# 만약 함수안에 전역변수와 지역변수의 이름이 동일하면
# 함수안에서는 지역변수가 우선적으로 이용된다. 코테에선 별로 신경ㄴㄴ
a = 0
def func():
    global a # 전역함수를 이용
    a += 1   # a가 1씩 증가시킴

for i in range(10): # 0~10까지
    func()          # func 10번 실행

print(a)

# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음
def operator(a,b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7,3)
print(a,b,c,d)
print(a)