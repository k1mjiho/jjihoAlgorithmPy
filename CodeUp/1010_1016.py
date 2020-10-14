# 1010
a = int(input())
print(a)
# 1011
b = input() # 사용자가 입력한 값은 문자열로 취급
print(b)
# 1012
c = float(input())
print("%f"%c)
# 1013
a, b = input().split() # 띄어쓰기(공백)로 구분, split으로 자르면 문자열
# b = int(input())
print(a,b)
# 1015 둘째자리까지 반올림하여 출력
a = float(input())
print("%.2f"%round(a,2)) # 1.00 입력시 1.0 -> 1.00으로 해결

