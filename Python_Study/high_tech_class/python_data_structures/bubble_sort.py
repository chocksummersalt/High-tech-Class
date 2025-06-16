"""
버블 정렬(Bubble Sort) 구현
- 인접한 두 요소를 비교하여 필요시 교환하는 방식으로 정렬하는 알고리즘
- 시간 복잡도: 평균 및 최악 O(n²), 최선 O(n)
- 공간 복잡도: O(1)
- 안정적인 정렬 알고리즘 (동일한 값의 상대적 순서가 유지됨)
"""

def bubble_sort(arr):
    """
    버블 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    # 최적화: 교환이 일어나지 않으면 이미 정렬된 상태
    for i in range(n):
        swapped = False
        
        # 각 패스에서 가장 큰 요소가 끝으로 이동하므로 
        # 이미 정렬된 부분은 비교할 필요 없음
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 교환이 일어나지 않았다면 이미 정렬된 상태
        if not swapped:
            break
    
    return arr


# 사용 예제
if __name__ == "__main__":
    import time
    import random
    
    # 테스트 데이터
    data = [64, 34, 25, 12, 22, 11, 90]
    
    print("버블 정렬 예제:")
    print(f"정렬 전: {data}")
    
    sorted_data = bubble_sort(data.copy())
    print(f"정렬 후: {sorted_data}")
    
    # 이미 정렬된 배열에서의 성능 (최선의 경우)
    already_sorted = list(range(100))
    
    start_time = time.time()
    bubble_sort(already_sorted.copy())
    best_case_time = time.time() - start_time
    
    print(f"\n최선의 경우 실행 시간 (이미 정렬된 100개 요소): {best_case_time:.6f}초")
    
    # 역순 정렬된 배열에서의 성능 (최악의 경우)
    reverse_sorted = list(range(100, 0, -1))
    
    start_time = time.time()
    bubble_sort(reverse_sorted.copy())
    worst_case_time = time.time() - start_time
    
    print(f"최악의 경우 실행 시간 (역순 정렬된 100개 요소): {worst_case_time:.6f}초")
    
    # 랜덤 배열에서의 성능 (평균적인 경우)
    random_data = list(range(100))
    random.shuffle(random_data)
    
    start_time = time.time()
    bubble_sort(random_data.copy())
    average_case_time = time.time() - start_time
    
    print(f"평균적인 경우 실행 시간 (무작위 100개 요소): {average_case_time:.6f}초")
    
    # 버블 정렬의 단계별 시각화
    print("\n버블 정렬 단계별 시각화:")
    example = [5, 1, 4, 2, 8]
    print(f"초기 배열: {example}")
    
    n = len(example)
    for i in range(n):
        for j in range(0, n - i - 1):
            # 현재 비교 중인 요소 표시
            current = example.copy()
            print(f"비교: {current[j]} > {current[j + 1]}?", end=" ")
            
            if current[j] > current[j + 1]:
                current[j], current[j + 1] = current[j + 1], current[j]
                example = current
                print(f"교환 -> {current}")
            else:
                print("교환 없음")
        
        print(f"패스 {i+1} 후: {example}")
