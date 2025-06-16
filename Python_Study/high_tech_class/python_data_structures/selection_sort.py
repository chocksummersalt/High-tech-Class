"""
선택 정렬(Selection Sort) 구현
- 배열에서 최소값을 찾아 맨 앞의 요소와 교환하는 방식으로 정렬하는 알고리즘
- 시간 복잡도: 항상 O(n²)
- 공간 복잡도: O(1)
- 불안정 정렬 알고리즘 (동일한 값의 상대적 순서가 바뀔 수 있음)
"""

def selection_sort(arr):
    """
    선택 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    for i in range(n):
        # 현재 위치부터 배열 끝까지 최소값의 인덱스 찾기
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 최소값을 현재 위치로 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


# 사용 예제
if __name__ == "__main__":
    import time
    import random
    
    # 테스트 데이터
    data = [64, 25, 12, 22, 11]
    
    print("선택 정렬 예제:")
    print(f"정렬 전: {data}")
    
    sorted_data = selection_sort(data.copy())
    print(f"정렬 후: {sorted_data}")
    
    # 이미 정렬된 배열에서의 성능
    already_sorted = list(range(100))
    
    start_time = time.time()
    selection_sort(already_sorted.copy())
    best_case_time = time.time() - start_time
    
    print(f"\n이미 정렬된 배열 실행 시간 (100개 요소): {best_case_time:.6f}초")
    
    # 역순 정렬된 배열에서의 성능
    reverse_sorted = list(range(100, 0, -1))
    
    start_time = time.time()
    selection_sort(reverse_sorted.copy())
    worst_case_time = time.time() - start_time
    
    print(f"역순 정렬된 배열 실행 시간 (100개 요소): {worst_case_time:.6f}초")
    
    # 랜덤 배열에서의 성능
    random_data = list(range(100))
    random.shuffle(random_data)
    
    start_time = time.time()
    selection_sort(random_data.copy())
    average_case_time = time.time() - start_time
    
    print(f"무작위 배열 실행 시간 (100개 요소): {average_case_time:.6f}초")
    
    # 선택 정렬의 단계별 시각화
    print("\n선택 정렬 단계별 시각화:")
    example = [64, 25, 12, 22, 11]
    print(f"초기 배열: {example}")
    
    n = len(example)
    for i in range(n):
        # 현재 위치부터 배열 끝까지 최소값의 인덱스 찾기
        min_idx = i
        for j in range(i + 1, n):
            if example[j] < example[min_idx]:
                min_idx = j
        
        # 최소값을 현재 위치로 교환
        print(f"최소값 {example[min_idx]}을(를) 인덱스 {i}의 {example[i]}와 교환")
        example[i], example[min_idx] = example[min_idx], example[i]
        print(f"패스 {i+1} 후: {example}")
    
    print("\n선택 정렬의 특징:")
    print("- 장점: 교환 횟수가 버블 정렬보다 적음 (최대 n-1번)")
    print("- 단점: 항상 O(n²) 시간 복잡도를 가짐 (최선의 경우에도 개선되지 않음)")
    print("- 불안정 정렬: 동일한 값의 상대적 순서가 바뀔 수 있음")
