def solution(skill, skill_trees):
    answer = 0

    for trees in skill_trees:
        flag = True
        queue = list(skill)
        # 스킬중에서 스킬트리에 있는거
        for t in trees:
            if t in skill:
                if t == queue[0]: # 만약 있으면 pop
                    queue.pop(0)
                else: # 그 순서 아니면 바로 false
                    flag = False
                    break
        if (flag):
            answer += 1

    return answer