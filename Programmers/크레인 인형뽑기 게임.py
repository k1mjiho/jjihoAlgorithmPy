def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            data = board[j][i - 1]

            if (data == 0):  # 빈값이면 다음 포문 돌려 밑에 인형 뽑기
                continue

            if (len(stack) > 0):  # 스택에 1개라도 있다면
                flag = isPop(stack, data)

                if (flag):  # 같은 인형이면
                    stack.pop()
                    answer += 2
                else:  # 다른 인형이면
                    stack.append(data)
            else:
                stack.append(data)  # 빈스택이면

            board[j][i - 1] = 0  # 인형뽑은 자리 0으로
            break  # 이제 인형은 뽑았으니까 moves 포문으로 나가기

    return answer


# 스택에 같은 인형있는지 알아보는 def
def isPop(stack, num):
    top = stack[-1]  # 스택 제일 위의 수
    if (top == num):
        return True
    else:
        return False


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))