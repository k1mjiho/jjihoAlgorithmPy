# 스택 : 먼저들어 온 데이터가 나중에 나가는 형식(LIFO)
# 삽입과 삭제로 구현된다 push, pop
# 입구와 출구가 동일한 형태
# 예) 박스쌓기

stack = []

# append pop 시간 복잡도 O(1)
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력(거꾸로)
print(stack) # 최하단 원소부터 출력