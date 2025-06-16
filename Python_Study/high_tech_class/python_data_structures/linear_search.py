"""
선형 탐색(Linear Search) 구현
- 배열의 각 요소를 순차적으로 확인하여 원하는 값을 찾는 알고리즘
- 시간 복잡도: O(n)
- 공간 복잡도: O(1)
"""

def linear_search(arr, target):
    """
    선형 탐색 알고리즘
    
    Args:
        arr: 탐색할 배열
        target: 찾고자 하는 값
    
    Returns:
        target의 인덱스, 없으면 -1 반환
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 사용 예제
if __name__ == "__main__":
    # 테스트 데이터
    data = [5, 2, 9, 1, 5, 6]
    
    print("선형 탐색 예제:")
    print(f"배열: {data}")
    
    # 존재하는 값 탐색
    target = 9
    result = linear_search(data, target)
    print(f"값 {target}의 인덱스: {result}")
    
    # 존재하지 않는 값 탐색
    target = 3
    result = linear_search(data, target)
    print(f"값 {target}의 인덱스: {result}")
    
    # 중복된 값의 경우 첫 번째 인덱스 반환
    target = 5
    result = linear_search(data, target)
    print(f"값 {target}의 첫 번째 인덱스: {result}")
    
    # 성능 테스트
    import time
    
    # 큰 배열에서의 성능 테스트
    large_data = list(range(100000))
    
    # 배열 끝에 있는 값 탐색 (최악의 경우)
    target = 99999
    start_time = time.time()
    result = linear_search(large_data, target)
    end_time = time.time()
    
    print(f"\n큰 배열에서 값 {target} 탐색 결과: 인덱스 {result}")
    print(f"탐색 시간: {(end_time - start_time) * 1000:.6f} 밀리초")
    
    # 배열에 없는 값 탐색
    target = 100001
    start_time = time.time()
    result = linear_search(large_data, target)
    end_time = time.time()
    
    print(f"큰 배열에서 값 {target} 탐색 결과: 인덱스 {result}")
    print(f"탐색 시간: {(end_time - start_time) * 1000:.6f} 밀리초")
