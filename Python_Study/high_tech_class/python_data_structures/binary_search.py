"""
이진 탐색(Binary Search) 구현
- 정렬된 배열에서 중간 값을 기준으로 탐색 범위를 절반씩 줄여가며 원하는 값을 찾는 알고리즘
- 시간 복잡도: O(log n)
- 공간 복잡도: O(1) (반복적 구현), O(log n) (재귀적 구현)
"""

def binary_search_iterative(arr, target):
    """
    반복적 이진 탐색 알고리즘
    
    Args:
        arr: 정렬된 배열
        target: 찾고자 하는 값
    
    Returns:
        target의 인덱스, 없으면 -1 반환
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    재귀적 이진 탐색 알고리즘
    
    Args:
        arr: 정렬된 배열
        target: 찾고자 하는 값
        left: 탐색 시작 인덱스
        right: 탐색 종료 인덱스
    
    Returns:
        target의 인덱스, 없으면 -1 반환
    """
    if left is None and right is None:
        left, right = 0, len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# 사용 예제
if __name__ == "__main__":
    # 테스트 데이터 (정렬된 배열)
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("이진 탐색 예제:")
    print(f"배열: {data}")
    
    # 반복적 이진 탐색
    print("\n반복적 이진 탐색:")
    
    # 존재하는 값 탐색
    target = 11
    result = binary_search_iterative(data, target)
    print(f"값 {target}의 인덱스: {result}")
    
    # 존재하지 않는 값 탐색
    target = 10
    result = binary_search_iterative(data, target)
    print(f"값 {target}의 인덱스: {result}")
    
    # 재귀적 이진 탐색
    print("\n재귀적 이진 탐색:")
    
    # 존재하는 값 탐색
    target = 15
    result = binary_search_recursive(data, target)
    print(f"값 {target}의 인덱스: {result}")
    
    # 존재하지 않는 값 탐색
    target = 12
    result = binary_search_recursive(data, target)
    print(f"값 {target}의 인덱스: {result}")
    
    # 성능 테스트
    import time
    
    # 큰 정렬된 배열에서의 성능 테스트
    large_data = list(range(0, 1000000, 2))  # 0, 2, 4, ..., 999998
    
    # 선형 탐색과 이진 탐색 비교
    from linear_search import linear_search
    
    target = 999998  # 배열의 마지막 요소
    
    # 선형 탐색 시간 측정
    start_time = time.time()
    linear_result = linear_search(large_data, target)
    linear_time = time.time() - start_time
    
    # 이진 탐색 시간 측정
    start_time = time.time()
    binary_result = binary_search_iterative(large_data, target)
    binary_time = time.time() - start_time
    
    print(f"\n큰 배열에서 값 {target} 탐색 결과:")
    print(f"선형 탐색: 인덱스 {linear_result}, 시간 {linear_time * 1000:.6f} 밀리초")
    print(f"이진 탐색: 인덱스 {binary_result}, 시간 {binary_time * 1000:.6f} 밀리초")
    print(f"이진 탐색이 선형 탐색보다 {linear_time / binary_time:.2f}배 빠름")
