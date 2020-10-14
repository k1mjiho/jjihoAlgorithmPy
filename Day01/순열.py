# 순열 : 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열하는 것
from itertools import permutations
data = ['A', 'B', 'C'] # 데이터 준비
# 모든 순열 구하기, a,b,c에서 3개를 골라 나열
result = list(permutations(data,3))
print(result)

# 중복 순열
from itertools import product
result2 = list(product(data, repeat=2))
print(result2)