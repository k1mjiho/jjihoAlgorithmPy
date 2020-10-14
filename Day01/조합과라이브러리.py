# 조합 : 서로다른 n개에서 순서에 상관 없이 서로다른 r개를 선택
from itertools import combinations
data = ['A', 'B', 'C'] # 데이터 준비
# 2개를 뽑는 모든 조합 구하기
result = list(combinations(data, 2))
print(result)

# 중복 조합
from itertools import combinations_with_replacement
result2 = list(combinations_with_replacement(data, 2))
print(result2)

# counter : 리스트와 같은 반복 가능한 객체가 주어졌을 때
# 내부의 원소가 몇 번씩 등장했는지 알려줌
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'red'])

print(counter['blue']) # blue가 등장한 횟수 출력
# 오,, 아마 int형으로 반환되나 보다 ㅇㅅㅇa
print(counter['red']+counter['blue'])
print(dict(counter)) # 사전 자료형으로 반환

# 최대 공약수와 최소 공배수
import math # 원주율, 제곱근, 팩토리얼 같은 함수도 포함하고 있음
# 최소 공배수(LCM)을 구하는 함수
def lcm(a,b):
    return a*b // math.gcd(a,b)
a, b =21, 14

print(math.gcd(21,14)) # 최대 공약수(GCD)
print(lcm(21,14))      # 최소 공배수(LCM)