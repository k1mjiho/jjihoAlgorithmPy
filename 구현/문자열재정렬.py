# 알고리즘 문제 풀 시 수와 숫자의 차이 구별
# 수 : 100 1000 같은 리얼 숫자데이터
# 숫자 : 0,1,2,3 ... 9 중 하나

# 첫째줄에 하나의 문자열 S가 주어진다
# 숫자는 다 합한값 마지막에
# 문자는 오름차순으로 출력
string = input()
result = []
sum = 0

for i in range(len(string)):
    if string[i].isdigit(): # 리스트의 요소가 숫자인지 확인
        sum += int(string[i])
    else:
        result.append(string[i])

result.sort()
result.append(str(sum))
print(''.join(result))

# 모범답안
data = input()
result = []
value = 0

# 문자 하나씩 확인
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha(x): # 리스트의 요소가 문자인지 확인
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))