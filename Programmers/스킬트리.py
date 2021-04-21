'''
2021-04-21 시간복잡도 해결해서 추가
filter, startswith 라이브러리 사용하기
list 안에 있는 지 확인할 때는 list보다 set을 사용하자 시간복잡도 O(N) -> O(1)로 줄일 수 있다
매개변수를 자신이 편한걸로 바꾸자
'''
def is_valid(skill, lst):
    if skill.startswith(lst):
        return True
    else:
        return False

def solution2(skills_order, candidates):
    answer = 0

    for candidate in candidates:
        filtered = filter(lambda skill: skill in skills_order, candidate)
        if is_valid(skills_order, ''.join(filtered)):
            answer += 1
    return answer


def solution1(skill, skill_trees):
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

