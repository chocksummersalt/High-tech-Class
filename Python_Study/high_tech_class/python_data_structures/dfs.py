"""
깊이 우선 탐색(DFS, Depth-First Search) 구현
- 그래프나 트리에서 한 경로를 끝까지 탐색한 후 다른 경로를 탐색하는 알고리즘
- 스택 또는 재귀를 사용하여 구현
- 시간 복잡도: O(V + E) (V: 정점 수, E: 간선 수)
- 공간 복잡도: O(V)
"""

def dfs_recursive(graph, start, visited=None):
    """
    재귀를 사용한 깊이 우선 탐색
    
    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 탐색 시작 정점
        visited: 방문한 정점 집합
    
    Returns:
        방문한 정점 리스트
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    스택을 사용한 깊이 우선 탐색
    
    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 탐색 시작 정점
    
    Returns:
        방문한 정점 리스트
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # 인접 정점을 스택에 추가 (역순으로 추가하여 작은 번호부터 방문)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


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
    
    print("깊이 우선 탐색(DFS) 예제:")
    print(f"그래프: {graph}")
    
    # 재귀적 DFS
    start_vertex = 'A'
    print(f"\n재귀적 DFS (시작 정점: {start_vertex}):")
    result = dfs_recursive(graph, start_vertex)
    print(f"방문 순서: {result}")
    
    # 반복적 DFS
    print(f"\n반복적 DFS (시작 정점: {start_vertex}):")
    result = dfs_iterative(graph, start_vertex)
    print(f"방문 순서: {result}")
    
    # 다른 시작 정점에서의 DFS
    start_vertex = 'C'
    print(f"\n재귀적 DFS (시작 정점: {start_vertex}):")
    result = dfs_recursive(graph, start_vertex)
    print(f"방문 순서: {result}")
    
    print(f"\n반복적 DFS (시작 정점: {start_vertex}):")
    result = dfs_iterative(graph, start_vertex)
    print(f"방문 순서: {result}")
    
    # 그래프 시각화 (ASCII)
    print("\n그래프 구조 (ASCII):")
    print("    A    ")
    print("   / \\   ")
    print("  B   C  ")
    print(" / \\   \\ ")
    print("D   E---F")
