"""
병합 정렬(Merge Sort) 구현
- 분할 정복 방식을 사용하는 정렬 알고리즘
- 배열을 절반으로 나누고 각각을 정렬한 후 병합하는 방식
- 시간 복잡도: 항상 O(n log n)
- 공간 복잡도: O(n)
- 안정적인 정렬 알고리즘 (동일한 값의 상대적 순서가 유지됨)
"""

def merge_sort(arr):
    """
    병합 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    if len(arr) <= 1:
        return arr
    
    # 배열을 절반으로 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 재귀적으로 각 절반을 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 정렬된 두 절반을 병합
    return merge(left_half, right_half)


def merge(left, right):
    """
    두 정렬된 배열을 병합
    
    Args:
        left: 첫 번째 정렬된 배열
        right: 두 번째 정렬된 배열
    
    Returns:
        병합된 정렬된 배열
    """
    result = []
    i = j = 0
    
    # 두 배열의 요소를 비교하여 작은 값부터 결과 배열에 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 남은 요소들 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# 제자리 병합 정렬 (추가 메모리 사용 최소화)
def merge_sort_in_place(arr):
    """
    제자리 병합 정렬 알고리즘 (래퍼 함수)
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    _merge_sort_in_place(arr, 0, len(arr) - 1)
    return arr


def _merge_sort_in_place(arr, start, end):
    """
    제자리 병합 정렬 알고리즘의 재귀적 구현
    
    Args:
        arr: 정렬할 배열
        start: 시작 인덱스
        end: 종료 인덱스
    """
    if start < end:
        mid = (start + end) // 2
        
        # 재귀적으로 각 절반을 정렬
        _merge_sort_in_place(arr, start, mid)
        _merge_sort_in_place(arr, mid + 1, end)
        
        # 정렬된 두 절반을 병합
        _merge_in_place(arr, start, mid, end)


def _merge_in_place(arr, start, mid, end):
    """
    두 정렬된 부분 배열을 제자리에서 병합
    
    Args:
        arr: 배열
        start: 첫 번째 부분 배열의 시작 인덱스
        mid: 첫 번째 부분 배열의 종료 인덱스
        end: 두 번째 부분 배열의 종료 인덱스
    """
    # 첫 번째 부분 배열을 임시 배열에 복사
    temp = arr[start:mid + 1]
    
    i = 0  # 임시 배열의 인덱스
    j = mid + 1  # 두 번째 부분 배열의 시작 인덱스
    k = start  # 결과 배열의 인덱스
    
    # 두 부분 배열의 요소를 비교하여 작은 값부터 결과 배열에 추가
    while i < len(temp) and j <= end:
        if temp[i] <= arr[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1
        k += 1
    
    # 첫 번째 부분 배열의 남은 요소들 추가
    while i < len(temp):
        arr[k] = temp[i]
        i += 1
        k += 1
    
    # 두 번째 부분 배열의 남은 요소들은 이미 올바른 위치에 있으므로 추가할 필요 없음


# 사용 예제
if __name__ == "__main__":
    import time
    import random
    
    # 테스트 데이터
    data = [38, 27, 43, 3, 9, 82, 10]
    
    print("병합 정렬 예제:")
    print(f"정렬 전: {data}")
    
    sorted_data = merge_sort(data.copy())
    print(f"정렬 후: {sorted_data}")
    
    # 제자리 병합 정렬
    in_place_data = data.copy()
    merge_sort_in_place(in_place_data)
    print(f"제자리 병합 정렬 후: {in_place_data}")
    
    # 성능 테스트
    array_size = 1000
    random_data = list(range(array_size))
    random.shuffle(random_data)
    
    # 병합 정렬 시간 측정
    start_time = time.time()
    merge_sort(random_data.copy())
    merge_sort_time = time.time() - start_time
    
    # 제자리 병합 정렬 시간 측정
    start_time = time.time()
    merge_sort_in_place(random_data.copy())
    in_place_time = time.time() - start_time
    
    # 퀵 정렬과 비교 (이전에 구현한 퀵 정렬 가져오기)
    from quick_sort import quick_sort
    
    start_time = time.time()
    quick_sort(random_data.copy())
    quick_sort_time = time.time() - start_time
    
    print(f"\n{array_size}개 요소 정렬 시간 비교:")
    print(f"병합 정렬: {merge_sort_time:.6f}초")
    print(f"제자리 병합 정렬: {in_place_time:.6f}초")
    print(f"퀵 정렬: {quick_sort_time:.6f}초")
    
    # 병합 정렬의 단계별 시각화
    print("\n병합 정렬 단계별 시각화:")
    example = [38, 27, 43, 3, 9, 82, 10]
    print(f"초기 배열: {example}")
    
    def visualize_merge_sort(arr, depth=0):
        print(f"{'  ' * depth}분할: {arr}")
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = visualize_merge_sort(arr[:mid], depth + 1)
        right = visualize_merge_sort(arr[mid:], depth + 1)
        
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        print(f"{'  ' * depth}병합: {left} + {right} -> {result}")
        return result
    
    visualize_merge_sort(example.copy())
    
    print("\n병합 정렬의 특징:")
    print("- 장점: 항상 O(n log n) 시간 복잡도 보장 (최악의 경우에도)")
    print("- 장점: 안정적인 정렬 알고리즘 (동일한 값의 상대적 순서 유지)")
    print("- 장점: 연결 리스트 정렬에 효율적")
    print("- 단점: 추가 메모리 공간 O(n) 필요")
    print("- 단점: 작은 배열에서는 오버헤드로 인해 삽입 정렬보다 느릴 수 있음")
    print("- 응용: 외부 정렬, 병렬 정렬 알고리즘의 기초")
