# 두 수험자가 푼 문제 수가 같다 -> 푼 문제 수가 5 미만인 경우는 제외
# 두 수험자가 푼 문제의 번호가 모두 같음, 점수가 같음
# 수험번호, 문제번호, 받은 점수를 나타내는 문자열 배열 logs
# 부정행위 의심자의 수험번호를 배열에 담고 사전순으로 정렬
# 부정수험자가 없는 경우에는 None으로 리턴

def solution2(logs):
    answer = []
    list = []
    new_li = []
    for i in logs:
        list.append(str(i[0:4]))
    # print(list)
    list_set = set(list)
    # 일단 5개이상 문제 맞춘애들을 뽑는다
    # 그리고서 문제의 수가 같을때
    for i in list_set:
        if list.count(i) >= 5:
            new_li.append(i)
    # print(new_li)
    # for i in logs:
    #     for j in new_li:
    #         if

    return answer

def solution(logs):
    data = {}
    answer = []
    students = []
    # n = len(logs)
    for l in logs:
        student, number, score = map(str, l.split())
        if student in data:
            data[student].append((int(number),int(score)))
        else:
            data[student] = [(int(number), int(score))]
            students.append(student)

    #학생 수
    length = len(data)

    for i in range(length-1):
        for j in range(i+1, length):
            #각각 다른 학생들 비교
            a = data[students[i]]
            b = data[students[j]]

            cnt = 0
            for index in range(len(a)):
                if b.count(a[index]) == 1:
                    cnt +=1

            if cnt >= 5:
                answer.append(students[i])
                answer.append(students[j])

    answer = list(set(answer))
    answer.sort()

    if len(answer) == 0:
        return ['None']
    else:
        return answer

print(solution(["1901 10 50", "1909 10 50"]))