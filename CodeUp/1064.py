# 정수 3개 인력받아 가장 작은 수 출력
# 삼항연산자 사용하기
a, b, c = map(int, input().split())
result = (b if a > b else a) > c and c or (b if a > b else a)
print(result)