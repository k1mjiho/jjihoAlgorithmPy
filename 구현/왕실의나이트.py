# 왕실의 나이트 : 완전탐색 + 구현
# 8X8 좌표평면
# 나이트는 말을 타고 있기때문에 이동을 할 때는 L자 형태로만 이동가능
# 이동방법 2가지
# 1. 수평으로 두칸 이동한 뒤에 수직으로 한칸 이동
# 2. 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동
# 나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력
# 행(세로) 1~8, 렬(가로) a~h
# dx = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# dy = [1, 2, 3, 4, 5, 6, 7, 8]
#
# where = list(input())
# count = 0

# 모범답안
# 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
# 지금 문자를 아스키코드로 변환 후 a를 빼주고 +1
# 문자를 숫자로 바꾸는 법
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (1,2), (-1,2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)