# 집합자료형 : 중복 X, 순서 X
# 인덱싱으로 값을 얻을 수 없다.
# 집합의 원소를 이용해 O(1)의 시간복잡도
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

# 합집합
print(a | b)
# 교집합
print(a & b)
# 차집합
print(a - b)
