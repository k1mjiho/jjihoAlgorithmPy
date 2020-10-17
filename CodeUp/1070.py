# 월 입력받아 계절 출력하깅
# python에는 switch문이 없다 if문을 활용해야함
a = int(input())
def switch(a):
    # 딕셔너리 자료형 이용
    # key : value
    dict_season = {
        1 : 'witer',
        2 : 'winter',
        3 : 'spring',
        4 : 'spring',
        5 : 'spring',
        6 : 'summer',
        7 : 'summer',
        8 : 'summer',
        9 : 'fall',
        10 : 'fall',
        11 : 'fall',
        12 : 'winter'
    }
    return dict_season.get(a)

print(switch(a))