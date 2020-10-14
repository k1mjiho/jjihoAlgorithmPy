# 1017
a = int(input())
print(a,a,a)

# 1019
a,b,c = input().split(".") # 자료형이 문자형임
a = int(a)
b = int(b)
c = int(c)
print("%04d"%a+"."+"%02d"%b+"."+"%02d"%c)

# 1020
a, b = input().split("-")
print(a+b)
# 1022
# input() 입력된 값에 따라서 정수의 타입을 정함
# raw_input() 입력된 값이 무엇이든 string으로 받음
from pip._vendor.distlib.compat import raw_input
a = raw_input()
print(a)

# 1023
a,b = input().split(".")
print(a)
print(b)

# 1024
str = input()
list_str = list(str) # 그냥 리스트로 변하는군,,,
for i in range(len(list_str)):
    print("\'"+list_str[i]+"\'")

# 1025
n = input()
list_n = list(n)
length = len(list_n)-1
for i in range(len(list_n)):
    print("["+str(int(list_n[i])*(10**length))+"]")
    length = length-1

# 1026
a,b,c = input().split(":")
b = int(b)
print(b)