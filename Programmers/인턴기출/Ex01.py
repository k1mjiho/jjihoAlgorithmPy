# 쇼핑몰에서 고객들이 주문한 상품을 배송
# 판매 주인 물품은 모두 n종류, 각 상품별로 1~n까지 번호가 있음
# 모든 고객 각자 2개씩 주문 -> 2종류 모두 재고가 있어야만 배송
# 둘 중 하나라도 재고가 없다면 두 상품 모두 배송ㄴㄴ
# 전체 상품의 갯수 n, 고객의 상품번호, 배송여부 2차원배열 delivery
# 재고 있으면 O 없으면 X 모르면 ? 출력
# 배송여부 1이면 배송 0이면 배송ㄴㄴ

def solution(n, delivery):
    answer = ''
    stock = []  # 재고가 있는것들의 리스트
    zero = []   # 재고가 없는애들의 리스트, 그리고 나머지 애들은 ?로 하면되겠지
    # 일단 1이면 그 배열의 0,1번째 상품은 재고 있는거임
    # 그럼 그거를 리스트에 저장
    for x in delivery:
        if x[2] == 1:
            stock.append(x[0])
            stock.append(x[1])
        # 0이면 0,1번째가 stock에 있는지 확인 그리고 없으면 zero에 넣는다
        elif x[2] == 0:
            if x[0] in stock:
                zero.append(x[1])
            elif x[1] in stock:
                zero.append(x[0])

    for i in range(1,n+1):
        if i in stock:
            answer += 'O'
        elif i in zero:
            answer += 'X'
        else:
            answer += '?'
    return answer

print(solution(7,[[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))