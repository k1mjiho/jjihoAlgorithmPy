# 문자열 S가 주어졌을 때, 왼->오 하나씩 모든 숫자 확인
# 곱하기 혹은 더하기 연산자를 만들 수 있는 가장 큰 수를 구하는 프로그램
# 모든 연산은 왼쪽부터 순서대로 이루어진다
str = input()
str_list = [int(i) for i in str]
result = str_list[0]
# str_list[i] != 0이면 곱하기
# str_list[i] == 0이면 더하기
for i in range(1,len(str_list)):
    if str_list[0] != 0: # 첫번째가 0이 아니고
        if str_list[i] != 0: #  그 다음수도 0이 아니면
            result = result*str_list[i]
        else:
            result += str_list[i]
    else:
        if i == 1:
            result += str_list[i]
        else:
            if str_list[i] != 0:  # 그 다음수도 0이 아니면
                result = result * str_list[i]
            else:
                result += str_list[i]
print(result)

# 모범답안
# 두 수 중에 하나라고 0 혹은 1인 경우, 더하기가 더 효율적
# 두 수가 모두 2이상인 경우에는 곱하기
data = input()

# 첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)