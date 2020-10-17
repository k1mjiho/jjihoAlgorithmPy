# 정수 3개 입력받아 짝수만 출력하기
num_list = list(map(int, input().split()))
for i in range(len(num_list)):
    if(num_list[i] % 2 == 0):
        print(num_list[i])