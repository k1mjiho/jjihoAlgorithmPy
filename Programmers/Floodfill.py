from collections import deque

def isVisitable(x, y, n, m, visited, image, prev_i):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and image[x][y] == prev_i

def bfs(n, m, x, y, image, visited):
    queue = deque()
    queue.append((x, y))  # 큐의 현재좌표 append

    while queue:
        x, y = queue.popleft()
        # 변화량이 고정되어있다면? const느낌의 변수 선언해서 사용
        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy

            # 좌표값 Validation
            # 존재하는 index이고 같은 색깔이라면
            if isVisitable(next_x, next_y, n, m, visited, image, image[x][y]):
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

def solution(n, m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:  # 방문하지 않은 좌표 체크
                answer += 1  # 구역의 첫번째 시작을 찾았다는 뜻
                visited[i][j] = True
                bfs(n, m, i, j, image, visited)  # 같은 구역에 있는 값을 회색으로 변환하는 함수
    return answer

