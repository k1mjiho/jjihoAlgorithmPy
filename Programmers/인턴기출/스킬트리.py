# 배열에 없는 스킬은 순서에 상관없이 배울 수 있다.
# 나머지는 선행 스킬 순서 skill에 있는 순서대로 배워야함
# skill_trees는 유저들이 만든 스킬트리 배열임
# 가능한 스킬 트리 개수를 리턴
# 하나씩 돌아가면서 확인하면 되니까 -> 그리디 알고리즘 같움ㅇㅅㅇ
# 스택이나 큐로 못푸나요?
# 런타임에러의 주된 이유: 배열의 index의 문제
from collections import deque

def solution(skill, skill_trees):
    answer = 0 # 가능한 스킬트리의 갯수
    # 만약 skilltrees에 skill에 있는 문자열 있으면 그것만 뽑아서 돌리자
    for x in skill_trees:
        str = deque()
        for i in range(len(x)):
            if x[i] in skill:
                str.append(x[i])

        # str은 trees에서 스킬들만 뽑은거임
        for j in skill:
            # print('i', i)
            # 만약 str이 skill의 0번째랑 값이 같으면 pop
            # 이거를 str 길이만큼 돌린다
            # str이 비어있으면 answer += 1
            if str.popleft() == j:
                if str:
                    continue
                else:
                    answer += 1
                    break
            else:
                break
            if str:
                continue
            else:
                break

    return answer

# def solution(skill, skill_trees):
#     answer = 0
#     skills = list(skill)
#
#     for tree in skill_trees:
#         count = 0
#         for i in range(len(skills)):
#             if tree.find(skills[i]) == -1:
#                 count += 1
#         if count == 3 or count == 0:
#             print(tree)
#             answer += 1
#         break
#
#     return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))