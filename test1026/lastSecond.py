# 문자열을 입력받으면
# 뒤에 두글자만 떼어서 
# reverse=True 이거하기
def lastLetters(word):
    str_list = list(word)
    length = len(str_list)
    slist = str_list[length-2:length]
    # print(' '.join(slist.__reversed__()))
    result = ' '.join(slist.__reversed__())
    return result

lastLetters('APPLE')