# 정수 n이 입력되고
# 00시 00분 00초부터 n시 59분 59초까지의 모든 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
# 0 <= n <= 23

from datetime import time

while True:
    # n이 범위 안에 들때까지 반복
    n = int(input())  # 시간
    if 0<=n and n<=23: # 조건이 맞다면 break
        break

# 파이썬에 시간함수가 있을까..?
# print(time(n)) 있움~~
count = 1
temp = 1
for i in range(n): # 시간에 3이 포함되어 있으면
    if str(i).__contains__('3'):
        count += 1
# 그리고 59분 59초에는 총 몇분이 들어가느냐,,
# 59에 3이 이만큼 들어가므로,
# 16*3
for i in range(59):
    if str(i).__contains__('3'):
        temp += 1

# 모범답안
# 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있음
# 단순히 시각을 1씩 증가 시키면서 3이 하나라도 포함되어 있는지 확인
# 완전탐색(Brute Forcing)유형 : 가능한 경우의 수를 모두 검사해보는 탐색 방법
# 하루는 86,400가지이다 -> 1초씩 증가 시키면서 3이 하나라도 포함되어있는지 확인

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
