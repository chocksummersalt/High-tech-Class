"""
퀵 정렬(Quick Sort) 구현
- 분할 정복 방식을 사용하는 정렬 알고리즘
- 피벗을 선택하고 피벗보다 작은 요소와 큰 요소로 분할한 후 재귀적으로 정렬
- 시간 복잡도: 평균 O(n log n), 최악 O(n²), 최선 O(n log n)
- 공간 복잡도: O(log n) (재귀 호출 스택)
- 불안정 정렬 알고리즘 (동일한 값의 상대적 순서가 바뀔 수 있음)
"""

def quick_sort(arr):
    """
    퀵 정렬 알고리즘 (래퍼 함수)
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    if len(arr) <= 1:
        return arr
    
    return _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, low, high):
    """
    퀵 정렬 알고리즘의 재귀적 구현
    
    Args:
        arr: 정렬할 배열
        low: 시작 인덱스
        high: 종료 인덱스
    
    Returns:
        정렬된 배열
    """
    if low < high:
        # 분할 인덱스 찾기
        pivot_idx = _partition(arr, low, high)
        
        # 분할된 부분 배열 정렬
        _quick_sort(arr, low, pivot_idx - 1)
        _quick_sort(arr, pivot_idx + 1, high)
    
    return arr


def _partition(arr, low, high):
    """
    배열을 피벗을 기준으로 분할
    
    Args:
        arr: 분할할 배열
        low: 시작 인덱스
        high: 종료 인덱스
    
    Returns:
        피벗의 최종 위치 인덱스
    """
    # 피벗으로 마지막 요소 선택
    pivot = arr[high]
    
    # 피벗보다 작은 요소들의 위치를 추적
    i = low - 1
    
    for j in range(low, high):
        # 현재 요소가 피벗보다 작거나 같으면 i를 증가시키고 교환
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 피벗을 올바른 위치에 배치
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


# 최적화된 퀵 정렬 (랜덤 피벗 선택)
def quick_sort_randomized(arr):
    """
    랜덤 피벗 선택을 사용한 퀵 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    import random
    
    if len(arr) <= 1:
        return arr
    
    def _partition_random(arr, low, high):
        # 랜덤 피벗 선택
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        return _partition(arr, low, high)
    
    def _quick_sort_random(arr, low, high):
        if low < high:
            pivot_idx = _partition_random(arr, low, high)
            _quick_sort_random(arr, low, pivot_idx - 1)
            _quick_sort_random(arr, pivot_idx + 1, high)
        return arr
    
    return _quick_sort_random(arr, 0, len(arr) - 1)


# 사용 예제
if __name__ == "__main__":
    import time
    import random
    
    # 테스트 데이터
    data = [10, 7, 8, 9, 1, 5]
    
    print("퀵 정렬 예제:")
    print(f"정렬 전: {data}")
    
    sorted_data = quick_sort(data.copy())
    print(f"정렬 후: {sorted_data}")
    
    # 이미 정렬된 배열에서의 성능 (최악의 경우가 될 수 있음)
    already_sorted = list(range(100))
    
    start_time = time.time()
    quick_sort(already_sorted.copy())
    sorted_case_time = time.time() - start_time
    
    print(f"\n이미 정렬된 배열 실행 시간 (100개 요소): {sorted_case_time:.6f}초")
    
    # 랜덤 배열에서의 성능 (평균적인 경우)
    random_data = list(range(100))
    random.shuffle(random_data)
    
    start_time = time.time()
    quick_sort(random_data.copy())
    average_case_time = time.time() - start_time
    
    print(f"무작위 배열 실행 시간 (100개 요소): {average_case_time:.6f}초")
    
    # 랜덤 피벗 선택을 사용한 퀵 정렬
    print("\n랜덤 피벗 선택을 사용한 퀵 정렬:")
    
    # 이미 정렬된 배열에서의 성능
    start_time = time.time()
    quick_sort_randomized(already_sorted.copy())
    random_pivot_sorted_time = time.time() - start_time
    
    print(f"이미 정렬된 배열 실행 시간 (100개 요소): {random_pivot_sorted_time:.6f}초")
    
    # 퀵 정렬의 단계별 시각화
    print("\n퀵 정렬 단계별 시각화:")
    example = [10, 7, 8, 9, 1, 5]
    print(f"초기 배열: {example}")
    
    def visualize_quick_sort(arr, low, high, depth=0):
        if low < high:
            print(f"{'  ' * depth}분할 범위: {arr[low:high+1]}")
            pivot = arr[high]
            print(f"{'  ' * depth}피벗: {pivot}")
            
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_idx = i + 1
            
            print(f"{'  ' * depth}분할 후: {arr[low:high+1]}")
            print(f"{'  ' * depth}피벗 위치: {pivot_idx}")
            
            visualize_quick_sort(arr, low, pivot_idx - 1, depth + 1)
            visualize_quick_sort(arr, pivot_idx + 1, high, depth + 1)
    
    example_copy = example.copy()
    visualize_quick_sort(example_copy, 0, len(example_copy) - 1)
    print(f"최종 정렬 결과: {example_copy}")
    
    print("\n퀵 정렬의 특징:")
    print("- 장점: 평균적으로 매우 빠른 정렬 알고리즘 O(n log n)")
    print("- 장점: 추가 메모리 공간을 거의 사용하지 않는 제자리 정렬")
    print("- 단점: 최악의 경우 O(n²) 시간 복잡도 (이미 정렬된 배열, 피벗 선택이 좋지 않은 경우)")
    print("- 단점: 불안정 정렬 (동일한 값의 상대적 순서가 바뀔 수 있음)")
    print("- 개선 방법: 랜덤 피벗 선택, 세 값의 중앙값을 피벗으로 선택, 작은 부분 배열에 삽입 정렬 사용")
