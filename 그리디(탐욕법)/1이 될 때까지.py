# N이 1이 될 때까지 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다
n, k = map(int, input().split())
count = 0
if n%k == 0:
    while(n != 1):
        count += 1
        n = n//k
else:
    while(n%k != 0):
        count += 1
        n = n-1
    while (n != 1):
        count += 1
        n = n // k
print(count)

# 모범답안
# 이케하면 시간복잡도 logO
n, k = map(int, input().split())
result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k # 몫에 k곱해서 가장가까운 수 구함
    result += (n-target) # 1을 빼는 연산의 횟수
    n = target
    # N이 K보다 적을 때(더 이상 나눌 수 없을때 반복문 탈출)
    if n < k:
        break # while문 무조건 참이여서 계속 수행하는걸 탈출
    # K로 나누기
    result += 1 # k로 나누는 연산 한번 더해주기
    n //= k

# N이 1보다 크다면?
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)