# 정수 1개 입력받아 분석하기
a = int(input())
if a>0:
    print('plus')
    if a % 2 == 0:
        print('even')
    else:
        print('odd')
else:
    print('minus')
    if a % 2 == 0:
        print('even')
    else:
        print('odd')
