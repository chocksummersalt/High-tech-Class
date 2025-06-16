"""
힙 정렬(Heap Sort) 구현
- 이진 힙 자료구조를 사용하는 정렬 알고리즘
- 최대 힙을 구성한 후 루트 노드(최댓값)를 배열 끝으로 이동하는 과정을 반복
- 시간 복잡도: 항상 O(n log n)
- 공간 복잡도: O(1) (제자리 정렬)
- 불안정 정렬 알고리즘 (동일한 값의 상대적 순서가 바뀔 수 있음)
"""

def heap_sort(arr):
    """
    힙 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    # 최대 힙 구성 (마지막 비단말 노드부터 시작)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 힙에서 요소를 하나씩 추출
    for i in range(n - 1, 0, -1):
        # 현재 루트(최댓값)를 배열 끝으로 이동
        arr[0], arr[i] = arr[i], arr[0]
        
        # 줄어든 힙에 대해 heapify 수행
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """
    주어진 노드를 루트로 하는 서브트리를 최대 힙으로 만드는 함수
    
    Args:
        arr: 배열
        n: 힙의 크기
        i: 현재 노드 인덱스
    """
    largest = i  # 현재 노드를 최댓값으로 초기화
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2  # 오른쪽 자식 노드
    
    # 왼쪽 자식이 루트보다 크면 largest 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # 오른쪽 자식이 현재까지의 최댓값보다 크면 largest 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # largest가 현재 노드가 아니면 교환하고 재귀적으로 heapify 수행
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# 파이썬 내장 heapq 모듈을 사용한 힙 정렬
def heap_sort_using_heapq(arr):
    """
    파이썬 heapq 모듈을 사용한 힙 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    import heapq
    
    # 최소 힙을 사용하므로 오름차순 정렬
    heap = []
    for value in arr:
        heapq.heappush(heap, value)
    
    return [heapq.heappop(heap) for _ in range(len(heap))]


# 사용 예제
if __name__ == "__main__":
    import time
    import random
    
    # 테스트 데이터
    data = [12, 11, 13, 5, 6, 7]
    
    print("힙 정렬 예제:")
    print(f"정렬 전: {data}")
    
    sorted_data = heap_sort(data.copy())
    print(f"정렬 후: {sorted_data}")
    
    # heapq 모듈을 사용한 힙 정렬
    heapq_sorted = heap_sort_using_heapq(data.copy())
    print(f"heapq 모듈 사용 정렬 후: {heapq_sorted}")
    
    # 성능 테스트
    array_size = 1000
    random_data = list(range(array_size))
    random.shuffle(random_data)
    
    # 힙 정렬 시간 측정
    start_time = time.time()
    heap_sort(random_data.copy())
    heap_sort_time = time.time() - start_time
    
    # heapq 모듈을 사용한 힙 정렬 시간 측정
    start_time = time.time()
    heap_sort_using_heapq(random_data.copy())
    heapq_sort_time = time.time() - start_time
    
    # 다른 정렬 알고리즘과 비교
    from quick_sort import quick_sort
    from merge_sort import merge_sort
    
    start_time = time.time()
    quick_sort(random_data.copy())
    quick_sort_time = time.time() - start_time
    
    start_time = time.time()
    merge_sort(random_data.copy())
    merge_sort_time = time.time() - start_time
    
    print(f"\n{array_size}개 요소 정렬 시간 비교:")
    print(f"힙 정렬: {heap_sort_time:.6f}초")
    print(f"heapq 모듈 사용 힙 정렬: {heapq_sort_time:.6f}초")
    print(f"퀵 정렬: {quick_sort_time:.6f}초")
    print(f"병합 정렬: {merge_sort_time:.6f}초")
    
    # 힙 정렬의 단계별 시각화
    print("\n힙 정렬 단계별 시각화:")
    example = [4, 10, 3, 5, 1]
    print(f"초기 배열: {example}")
    
    def visualize_heap(arr, n, i, depth=0):
        """힙 구조를 시각화하는 함수"""
        if i < n:
            left = 2 * i + 1
            right = 2 * i + 2
            
            print(f"{'  ' * depth}노드 {arr[i]}")
            
            if left < n:
                print(f"{'  ' * (depth+1)}왼쪽 자식: {arr[left]}")
                visualize_heap(arr, n, left, depth + 2)
            
            if right < n:
                print(f"{'  ' * (depth+1)}오른쪽 자식: {arr[right]}")
                visualize_heap(arr, n, right, depth + 2)
    
    # 최대 힙 구성 과정 시각화
    print("\n최대 힙 구성 과정:")
    example_copy = example.copy()
    n = len(example_copy)
    
    print("초기 배열 상태:")
    visualize_heap(example_copy, n, 0)
    
    for i in range(n // 2 - 1, -1, -1):
        print(f"\n노드 {example_copy[i]}에 대해 heapify 수행:")
        heapify(example_copy, n, i)
        print(f"배열 상태: {example_copy}")
        visualize_heap(example_copy, n, 0)
    
    print("\n최대 힙 구성 완료:", example_copy)
    
    # 정렬 과정 시각화
    print("\n정렬 과정:")
    for i in range(n - 1, 0, -1):
        example_copy[0], example_copy[i] = example_copy[i], example_copy[0]
        print(f"최댓값 {example_copy[i]}를 위치 {i}로 이동: {example_copy}")
        
        heapify(example_copy, i, 0)
        print(f"남은 힙에 대해 heapify 수행: {example_copy}")
    
    print("\n최종 정렬 결과:", example_copy)
    
    print("\n힙 정렬의 특징:")
    print("- 장점: 항상 O(n log n) 시간 복잡도 보장")
    print("- 장점: 추가 메모리 공간을 사용하지 않는 제자리 정렬")
    print("- 장점: 우선순위 큐 구현에 활용 가능")
    print("- 단점: 불안정 정렬 (동일한 값의 상대적 순서가 바뀔 수 있음)")
    print("- 단점: 캐시 지역성이 좋지 않아 실제로는 퀵 정렬이나 병합 정렬보다 느릴 수 있음")
