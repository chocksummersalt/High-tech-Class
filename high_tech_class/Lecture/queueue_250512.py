#queue ADT

items = []

def isEmpty():
    return len(items) == 0 #비어있으면 불린 반환

def enqueue(item): #항목을 쿠의 맨 뒤에 추가한다. 
    items.append(item)

def dequeue(): #큐의 맨 앞에 있는 항목을 꺼내 반환한다.
    if not isEmpty():
        return items.pop()
    
def peek(): # 큐의 맨 앞에 있는 항목을 삭제하지 않고 반환 한다.
    if not isEmpty(): return items[-1]

def size(): #큐의 모든 항목들의 갯수를 반환한다.
    return len(items)

def clear(): #큐를 공백으로 만든다.
    global items; items = []



#circular queue

max_qsize = 10

class circularqueue :
    def __init__(self):
        self. front = 0
        self. rear = 0
        self. items = [None] * max_qsize #빈칸 리스트 10개 생성 

        def isEmpty(self) : return self. front == self.rear #앞이랑 뒤랑 같아?
        def isfull(self) : return self.front == (self.rear+1) %max_qsize #포화상태? 
        #한번 사용할 때 마다 한칸씩 가다가 max만나면 0번째가 되는. 그리고 포화확인위해서 0번째는 비워둠



#미로 게임

from collections import deque  # 큐 구현에 사용

# 미로
maze = [['1','1','1','1','1','1'],
        ['e','0','0','0','0','0'],
        ['1','0','1','0','1','1'],
        ['1','1','1','0','0','x']]

maze_size = 4

# BFS 미로 탐색
def bfs(maze, maze_size):
    start = None
    end = None

    # 시작점과 도착점 찾기
    for r in range(maze_size):
        for c in range(len(maze[r])):
            if maze[r][c] == 'e':
                start = (r, c)
            elif maze[r][c] == 'x':
                end = (r, c)

    # 큐 초기화
    queue = deque()
    queue.append((start[0], start[1], 0))  # (행, 열, 이동거리)
    visited = [[False]*len(maze[0]) for _ in range(maze_size)]
    visited[start[0]][start[1]] = True

    # 이동 방향 (상하좌우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, steps = queue.popleft()

        if (r, c) == end:
            return steps  # 최단 거리 반환

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < maze_size and 0 <= nc < len(maze[0]):
                if not visited[nr][nc] and maze[nr][nc] != '1':
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))

    return -1  # 도달 불가

# 실행
result = bfs(maze, maze_size)

if result != -1:
    print(f"목표지점까지 최단경로는 {result}번 이동입니다.")
else:
    print("목표지점에 도달할 수 없습니다.")
