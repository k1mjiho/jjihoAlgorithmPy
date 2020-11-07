# 문자열의 길이가 4라면 data는 길이가 4인 이진원소들로 합쳐진 문자열
# data르르 포장한다는것은 penter + data + pexit
# 만약 data에 문자열들과 동일한 원소가 있다면 -> pescape를 앞에 붙여줘야 함
# 아아 이거 data를 penter의 크기대로 잘라서 비교해야됨
# 데이터 잘라서 비교하고 똑같은거 있으면 앞에 pescape붙이기

def solution(penter, pexit, pescape, data):
    answer = ''
    length = len(penter)
    ran = int(len(data) / length)
    answer = penter
    # 일단 data를 penter의 크기대로 잘라서 penter, pexit와 비교한다
    # 그리고 같으면 원소 앞에 pescape를 붙인다 아니면 그냥 continue
    for i in range(0,ran):
        if i == 0:
            if data[0:length] == penter or data[0:length] == pexit or data[0:length] == pescape:
                answer += pescape + data[0:length]
            else:
                answer += data[0:length]
        else:
            if data[i*length: length*(i+1)] == penter or data[i*length: length*(i+1)] == pexit or data[i*length: length*(i+1)] == pescape:
                answer += pescape + data[i*length: length*(i+1)]
            else:
                answer += data[i*length: length*(i+1)]

    answer = answer + pexit
    return answer

print(solution("10", "11", "00", "00011011"))