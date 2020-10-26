# 숫자로 이루어진 배열은 받는다
# 그래서 거기에서 제일 작은 수를 찾는다
# 어디까지의 합이 배열의 마지막 인덱스값과 같은가?

def balancedSum(arr):
    length = len(arr)
    result = arr[length-1]
    sum = 0

    for i in range(2,length):
        sum += arr[i]
        if(result == sum):
            return i

list = [1,2,3,3]
print(balancedSum(list))