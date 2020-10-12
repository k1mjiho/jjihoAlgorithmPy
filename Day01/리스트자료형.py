# 직접 데이터를 넣어 초기화
a = [1,2,3,4,5,6,7,8,9]
print(a)
# 네번째 원소만 출력
print(a[3])
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

a = [1,2,3,4,5,6,7,8,9]
# 리스트의 특정한 원소에 접근하는 것을 인덱싱
# 여덟번째 원소 출력
print(a[7])
# 파이썬에서 음의 정수로 접근 시 거꾸로 출력
# 뒤에서 첫번째 원소 출력
print(a[-1])
# 뒤에서 세 번째 원소 출력
print(a[-3])

# 연속적인 위치를 갖는 원소들을 가져와야할 때는 슬라이싱 이용
# 네번째 원소 출력
print(a[3])
# 두번째 원소부터 네번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션 : 초기화하는 방법 중 하나 (2차원 리스트 초기화시 유용)
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)
# 1부터 9까지의 수들의 제곱값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# n X m 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)
array[1][1] = 5
print(array)

# _ 언제사용? : 반복하는데 반복을 위한 변수의 값 무시하고자 할 때
for _ in range(3):
    print("Hello World")

a = [1,4,3]
# 리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)
# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)
# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬 : ", a)
# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 : ", a)
# 특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3추가", a)
# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", a.count(3))
# 특정 값 데이터 삭제
a.remove(3)
print("값이 3인 데이터 삭제 (여러개이면 하나만 삭제 됨)", a)
# 리스트에서 특정 값을 가지는 원소 모두 제거하기
a = [1,2,3,4,5,6,5,5]
# 3이랑 5가 포함되지않은 리스트 구하기
remove_set = {3,5} # 집합 자료형
# remove_list에 포함되지않은 값만 저장
result = [i for i in a if i not in remove_set]
print(result)

# 리스트의 길이 출력
print(len(a))