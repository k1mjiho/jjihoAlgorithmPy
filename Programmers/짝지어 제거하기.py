'''
1. s에서 하나씩 뽑아 스택에 쌓는다.
2. 이때 스택에 넣을때 스택의 제일 위에 원소랑 같으면 push ㄴㄴ 위에 원소도 pop
'''

def solution(s):
    answer = 0
    s = list(s)
    stack = []

    while len(s) > 0:
        tmp = s.pop()
        if stack:  # s가 존재한다면
            if stack[-1] == tmp:
                stack.pop()
        else:
            stack.append(tmp)

    if len(stack) == 0:
        answer = 1

    return answer