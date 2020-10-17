# 두 정수 입력받아 큰 수 출력
# 삼항연산자 사용하기
a, b = map(int, input().split())
# result = a > b and a or b
result = a if (a>b) else b
print(result)