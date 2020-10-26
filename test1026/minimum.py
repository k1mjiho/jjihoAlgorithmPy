# 리스트의 len + sum 값 구하는거
# 처음에 리스트의 길이 입력받아서 배열 생성
# 그리고 하나씩 입력받아서 배열 생성하고
# 그거의 총합 구하기
# 그리고 길이 수 더해서 출력
# sum(arr) 이케 하면 됨

def minX(arr):
    a = len(arr)

    result = a + sum(arr)
    return result