# 입력된 수가 소수냐 아니냐
# 소수면 1반환
# 아니면 그 약수중에서 제일 작은 수 반환
# x = int(input())
# def isPrime2(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True
# print(isPrime2(x))

# 숫자가 주어진다 만약 이 숫자가 소수라면 1 반환
# 1보다 크지만 제일 작은 약수를 반환한다.
# 소수 -> 약수가 자기 자신이랑 1만 있는 수
def isPrime(n):
    for i in range(1, n):
        if (n % i) == 0:
            return i
        else:
            return 1
print(isPrime(3))