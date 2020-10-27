# 먼저 들어 온 데이터가 먼저 나가는 형식(FIFO)
# 입구와 출구가 모두 뚫려 있는 터널과 같은 형태
# 기능적으로 큐 구현 가능하지만
# 시간복잡도 때문에 deque라이브러리를 사용한당
from collections import deque

# 큐 구현을 위해 deque 라이브러리 적용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 가장 왼쪽에 있는 요소를 삭제 O(1)
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력