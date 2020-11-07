# 로봇청소기 -> 대각선, 지그재그 모양의 동선에서 움직이면서 청소
# 수평 수직은 1칸당 1초, 대각선 방향으로 이동하는데 1칸당 2초
# 방의 한변의 길이 n , 오른쪽인지 아래쪽인지 horizontal = T/F
# 각 칸마다 몇초 걸리는지 배열로 반환하기

def solution(n, horizontal):
    answer = [[]]
    bot = 0
    # 오른쪽으로 가는거면 True
    if horizontal: # 오른쪽으로 가는거면
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0: # 두개 다 0일때 이렇게
                    answer[0].append(bot)
                    bot += 1
                else:
                    answer[0].append

    return answer

print(solution(4, True))
