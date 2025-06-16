"""
너비 우선 탐색(BFS, Breadth-First Search) 구현
- 그래프나 트리에서 가까운 정점부터 탐색하는 알고리즘
- 큐를 사용하여 구현
- 시간 복잡도: O(V + E) (V: 정점 수, E: 간선 수)
- 공간 복잡도: O(V)
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색 알고리즘
    
    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 탐색 시작 정점
    
    Returns:
        방문한 정점 리스트
    """
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # 인접 정점을 큐에 추가
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result


def bfs_with_distance(graph, start):
    """
    거리 정보를 포함한 너비 우선 탐색 알고리즘
    
    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 탐색 시작 정점
    
    Returns:
        각 정점까지의 최단 거리를 담은 딕셔너리
    """
    visited = set([start])
    queue = deque([(start, 0)])  # (정점, 거리) 쌍
    distances = {start: 0}
    
    while queue:
        vertex, distance = queue.popleft()
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))
    
    return distances


def shortest_path(graph, start, end):
    """
    BFS를 사용하여 두 정점 사이의 최단 경로 찾기
    
    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 정점
        end: 도착 정점
    
    Returns:
        최단 경로 리스트, 경로가 없으면 None 반환
    """
    if start == end:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])  # (정점, 경로) 쌍
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # 경로가 없는 경우


# 사용 예제
if __name__ == "__main__":
    # 인접 리스트로 표현된 그래프
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("너비 우선 탐색(BFS) 예제:")
    print(f"그래프: {graph}")
    
    # 기본 BFS
    start_vertex = 'A'
    print(f"\nBFS (시작 정점: {start_vertex}):")
    result = bfs(graph, start_vertex)
    print(f"방문 순서: {result}")
    
    # 다른 시작 정점에서의 BFS
    start_vertex = 'C'
    print(f"\nBFS (시작 정점: {start_vertex}):")
    result = bfs(graph, start_vertex)
    print(f"방문 순서: {result}")
    
    # 거리 정보를 포함한 BFS
    start_vertex = 'A'
    print(f"\n거리 정보를 포함한 BFS (시작 정점: {start_vertex}):")
    distances = bfs_with_distance(graph, start_vertex)
    for vertex, distance in distances.items():
        print(f"{vertex}까지의 거리: {distance}")
    
    # 최단 경로 찾기
    start_vertex = 'A'
    end_vertex = 'F'
    print(f"\n{start_vertex}에서 {end_vertex}까지의 최단 경로:")
    path = shortest_path(graph, start_vertex, end_vertex)
    print(f"경로: {path}")
    
    # 그래프 시각화 (ASCII)
    print("\n그래프 구조 (ASCII):")
    print("    A    ")
    print("   / \\   ")
    print("  B   C  ")
    print(" / \\   \\ ")
    print("D   E---F")
