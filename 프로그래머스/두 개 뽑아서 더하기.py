
'''
enumerate는 리스트를 인덱스와 해당 데이터 값 두개를 다 뽑아올 수 있음
생각해보면 이 문제는 순열인거같다
배열에서 2개를 뽑을 수 있는 경우의 수를 다 뽑아서 그 합을 구하는게 아닐깡,,
'''

# ver1. 직관적으로 그냥 이중포문 돌리기
def solution1(numbers):
    answer = []
    length = len(numbers)
    cnt = 0

    for i in numbers:
        cnt = cnt + 1
        for j in numbers[cnt: length]:
            sum = i + j
            answer.append(sum)

    answer = list(set(answer))
    answer.sort()

    return answer

# ver2. enumerate 사용해서 이중 포문 돌리기
def solution2(numbers):
    answer = []

    for idx, num in enumerate(numbers, 1):
        for num2 in numbers[idx:]:
            sum = num + num2
            answer.append(sum)

    answer = list(set(answer))
    answer.sort()

    return answer

print(solution1([2,1,3,4,1]))