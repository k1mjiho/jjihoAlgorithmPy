# for 변수 in 리스트:
#   실행할 소스코드
array = [9,8,7,6,5]

for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회 시 range()
result = 0
# i는 1~9까지의 값을 순회
for i in range(1,10):
    result += i
print("range() 사용 :",result)

# continue 키워드 : 남은 코드의 실행을 건너뛰고, 다음 반복을 진행
result = 0
for i in range(1,10):
    if i % 2 == 0:
        continue # i가 짝수이면 그냥 건너뛰기
    result += i
print("continue 키워드 사용 :",result)

# 중첩된 반복문 : 구구단 예제
# for i in range(1,10):
#     for j in range(1,10):
#         print(i,"X",j,"=",i*j)
#     print()