# 1~9까지 모든 정수의 합 구하기(while문)
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# 1~9까지 홀수의 합 구하기
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1 # 들여쓰기 유의!!

print(result)