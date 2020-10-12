# 한줄의 문자열을 입력받는 함수
# input()
# 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 공백을 기준으로 구분된 데이터를 입력받을때
# list(map(int, input().split()))
# 공백을 기준으로 구분된 데이터의 개수가 많지않다면, 단순히
# a, b, c = map(int, input().split())

# 데이터의 개수 입력
import sys

n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

# 빠르게 입력받아야할때
data = sys.stdin.readline().rstrip()
print(data)

answer = 7
print(f"정답은 {answer}입니다.")
# 출력할 변수
print("정답은",answer,"입니다.")
print("정답은 " + str(answer) + "입니다.")