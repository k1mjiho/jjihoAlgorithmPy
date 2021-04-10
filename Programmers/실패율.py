'''
처음에는 for문으로 다 돌려서 풀었는데
파이썬에 count라이브러리가 있었음
count 배열에 해당하는 수가 몇개 있는지 세어주는 라이브러리
시간복잡도 O(N)
오랜만에 시간복잡도에 생각 할 수 있는 계기가 되었다
'''

def solution1(N, stages):
    answer = []
    len_s = len(stages)
    dic = {}

    for user in stages:
        for stage in range(1, N + 1):
            if (len(dic) < stage):  # dic 함수 초기화
                dic[stage] = 0
            if (stage == user):  # user가 어디에 있는지 
                dic[stage] += 1

    # 각 단계별로 실패율 구하기
    for i in range(1, len(dic) + 1):
        temp = dic[i]

        if (len_s == 0):
            dic[i] = 0
            continue

        dic[i] = temp / len_s
        len_s -= temp

    # 이제 value값으로 sort하고
    dic = sorted(dic.items(), key=(lambda x: x[1]), reverse=True)
    # key값 answer에 넣어주기
    for i in dic:
        answer.append(i[0])

    return answer

def solution2(N, stages):
    dic = {}
    len_s = len(stages)

    for stage in range(1, N + 1):

        if (len_s == 0):
            dic[stage] = 0
        else:
            dic[stage] = stages.count(stage) / len_s
            len_s -= stages.count(stage)

    return sorted(dic, key=lambda x: dic[x], reverse=True)
