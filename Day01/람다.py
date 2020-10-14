# 특정한 기능을 수행하는 삼수를 한 줄에 작성할 수 있다는 점
# 일반적으로 add() 메소드 사용에서
# 람다 표현식으로 구현한 add() 메소드
print((lambda a, b: a+b)(3,7))

# 내장 함수에서 자주 사용되는 람다 함수
# 리스트, 리스트 안의 원소는 튜플형태로 존재
# 튜플? (키,값)
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key)) # 정렬기준을 2번째원소를 기준으로 정렬
print(sorted(array, key=lambda x : x[1]))

# 여러개의 리스트에 동일한 규칙을 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
# map? 각각의 원소에 어떠한 함수를 적용
result = map(lambda a,b: a+b, list1, list2)
print(list(result))