# 정수 3개 입력받아 합과 평균 출력
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a+b+c)
print(round((a+b+c)/3,1))

# map 이용해서 해보기
li = list(map(int, input().split()))
for i in range(len(li)):
    sum