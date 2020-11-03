# n명의 사람이 영어 끝말잇기 2이상 10이하
# 자신이 몇번째 끝말잇기하고 있는지 기억해야함
# 그전에 나온 단어 말하면 탈락임 -> 말했던 단어 다 기억해놔야 함
# 가장 먼저 탈락하는 사람이 자신의 몇번째에 탈락하는지 구하기

def solution(n, words):
    answer = [0,0] # [몇번째 사람?, 몇번째 게임?]
    for i in range(len(words)):
        # 0이면 나눌수 없으니까
        if i == 0:
            continue
        # 끝말잇기 불가능 하거나 똑같은 단어가 나왔을때
        elif words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            answer = [i%n +1,i//n + 1]
            break

    return answer

print(solution(2,['hello', 'oer', 'rw', 'wever', 'rw', 'world', 'draw']))