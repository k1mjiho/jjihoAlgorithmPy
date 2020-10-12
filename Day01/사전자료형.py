# 키와 값의 쌍을 데이터로 가지는 자료형
# 순차적으로 저장되는 리스트와 대조적
# 해시테이블 이용 -> 데이터 조회/수정 O(1)의 시간복잡도
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Conconut'

print(data)

if '사과' in data :
    print('"사과"를 키로 가지는 데이터가 존재')

b = {
    '김지호' : 90,
    '정예원' : 97
}
print(b)
# key 데이터만 뽑을때는 keys()
# value 데이터만 뽑을때는 values()
keys_list = b.keys()
print(keys_list)
# 리스트로 변환
print(list(keys_list))

