"""
삽입 정렬(Insertion Sort) 구현
- 정렬된 부분과 정렬되지 않은 부분으로 나누어 정렬되지 않은 요소를 정렬된 부분의 적절한 위치에 삽입하는 알고리즘
- 시간 복잡도: 평균 및 최악 O(n²), 최선 O(n)
- 공간 복잡도: O(1)
- 안정적인 정렬 알고리즘 (동일한 값의 상대적 순서가 유지됨)
"""

def insertion_sort(arr):
    """
    삽입 정렬 알고리즘
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # key보다 큰 요소들을 오른쪽으로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # key를 적절한 위치에 삽입
        arr[j + 1] = key
    
    return arr


# 사용 예제
if __name__ == "__main__":
    import time
    import random
    
    # 테스트 데이터
    data = [12, 11, 13, 5, 6]
    
    print("삽입 정렬 예제:")
    print(f"정렬 전: {data}")
    
    sorted_data = insertion_sort(data.copy())
    print(f"정렬 후: {sorted_data}")
    
    # 이미 정렬된 배열에서의 성능 (최선의 경우)
    already_sorted = list(range(100))
    
    start_time = time.time()
    insertion_sort(already_sorted.copy())
    best_case_time = time.time() - start_time
    
    print(f"\n최선의 경우 실행 시간 (이미 정렬된 100개 요소): {best_case_time:.6f}초")
    
    # 역순 정렬된 배열에서의 성능 (최악의 경우)
    reverse_sorted = list(range(100, 0, -1))
    
    start_time = time.time()
    insertion_sort(reverse_sorted.copy())
    worst_case_time = time.time() - start_time
    
    print(f"최악의 경우 실행 시간 (역순 정렬된 100개 요소): {worst_case_time:.6f}초")
    
    # 랜덤 배열에서의 성능 (평균적인 경우)
    random_data = list(range(100))
    random.shuffle(random_data)
    
    start_time = time.time()
    insertion_sort(random_data.copy())
    average_case_time = time.time() - start_time
    
    print(f"평균적인 경우 실행 시간 (무작위 100개 요소): {average_case_time:.6f}초")
    
    # 삽입 정렬의 단계별 시각화
    print("\n삽입 정렬 단계별 시각화:")
    example = [12, 11, 13, 5, 6]
    print(f"초기 배열: {example}")
    
    for i in range(1, len(example)):
        key = example[i]
        j = i - 1
        print(f"\n현재 삽입할 요소: {key}")
        print(f"정렬된 부분: {example[:i]}, 정렬되지 않은 부분: {example[i:]}")
        
        # key보다 큰 요소들을 오른쪽으로 이동
        while j >= 0 and example[j] > key:
            example[j + 1] = example[j]
            j -= 1
            print(f"  이동: {example}")
        
        # key를 적절한 위치에 삽입
        example[j + 1] = key
        print(f"삽입 후: {example}")
    
    print("\n삽입 정렬의 특징:")
    print("- 장점: 작은 데이터셋에서 효율적, 이미 정렬된 데이터에 대해 O(n) 시간 복잡도")
    print("- 장점: 안정적인 정렬 알고리즘 (동일한 값의 상대적 순서 유지)")
    print("- 장점: 온라인 알고리즘 (데이터가 들어오는 대로 정렬 가능)")
    print("- 단점: 큰 데이터셋에서는 비효율적 (O(n²) 시간 복잡도)")
