'''
조건을 잘 생각
1. ( 괄호의 시작을 배열에 담는다
2. ) 가 있으려면 ( 하나 이상은 있어야 한다
3. ( 갯수가 ) 보다 모자르면 False
'''

def solution(s):
    s = list(s)
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0