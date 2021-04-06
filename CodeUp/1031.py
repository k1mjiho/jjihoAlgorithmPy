# 10진수 1개 입력
# 8진수로 출력하기
a = input()
# n = int(a)
# print("%o"%n) # 8진수로 변환해준다

b = format(a, '#b')
print(b)