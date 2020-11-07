# 돈 잃으면 다음판에는 잃은 돈의 두배를 다시 베팅해야 함
# 이 전략으로 동전 앞뒤 맞추기 게임에서 이 베팅법 사용했을 때 돈을 얼마나 딸 수 있는가
# 첫판에는 항상 100원을 건다 -> 연속해서 지는 도중에 한번이라도 이기면 다시 100원 베팅
# 전에 져서 두배 걸어야하는데 돈 모자르면 남은 돈 전부를 건다고 가정
# 모두 잃으면 즉시 게임 중단
# 초기 금액 money 내가 예측한 동전의 면을 순서대로 나타낸 배열 expected, 실제 배열 actual
# 게임이 끝나고 남은 금액을 리턴, money 와 actual 배열의 길이 같다
# 배열 앞뒤면 H, T로 나타낸다

def solution(money, expected, actual):
    answer = -1
    # 처음에는 100원을 건다
    # flag = True
    initial = 100
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            # 예상이 맞으면 intial 돈을 money에 더한다
            money += initial
            initial = 100
        else:
            money -= initial
            initial = initial*2
            if money - initial < 0:
                initial = money
    return money

print(solution(1000,['H', 'T', 'H', 'T', 'H', 'T', 'H'],['T', 'T', 'H', 'H', 'T', 'T', 'H']))

