"""
자료구조 및 알고리즘 테스트 스크립트
- 구현한 모든 자료구조와 알고리즘을 테스트하고 검증
"""

import os
import time
import random
import sys

def print_header(title):
    """테스트 섹션 헤더 출력"""
    print("\n" + "=" * 60)
    print(f" {title} ".center(60, "="))
    print("=" * 60)

def test_data_structure(name, module_name):
    """자료구조 모듈을 테스트"""
    print_header(f"{name} 테스트")
    try:
        os.system(f"python3 {module_name}.py")
        print(f"\n✅ {name} 테스트 성공")
        return True
    except Exception as e:
        print(f"\n❌ {name} 테스트 실패: {e}")
        return False

def test_search_algorithm(name, module_name):
    """탐색 알고리즘 모듈을 테스트"""
    print_header(f"{name} 테스트")
    try:
        os.system(f"python3 {module_name}.py")
        print(f"\n✅ {name} 테스트 성공")
        return True
    except Exception as e:
        print(f"\n❌ {name} 테스트 실패: {e}")
        return False

def test_sort_algorithm(name, module_name):
    """정렬 알고리즘 모듈을 테스트"""
    print_header(f"{name} 테스트")
    try:
        os.system(f"python3 {module_name}.py")
        print(f"\n✅ {name} 테스트 성공")
        return True
    except Exception as e:
        print(f"\n❌ {name} 테스트 실패: {e}")
        return False

def compare_sorting_algorithms():
    """여러 정렬 알고리즘의 성능 비교"""
    print_header("정렬 알고리즘 성능 비교")
    
    # 정렬 알고리즘 모듈 가져오기
    sys.path.append(os.getcwd())
    from bubble_sort import bubble_sort
    from selection_sort import selection_sort
    from insertion_sort import insertion_sort
    from quick_sort import quick_sort
    from merge_sort import merge_sort
    from heap_sort import heap_sort
    
    # 테스트 데이터 생성
    sizes = [100, 1000, 5000]
    algorithms = [
        ("버블 정렬", bubble_sort),
        ("선택 정렬", selection_sort),
        ("삽입 정렬", insertion_sort),
        ("퀵 정렬", quick_sort),
        ("병합 정렬", merge_sort),
        ("힙 정렬", heap_sort)
    ]
    
    for size in sizes:
        print(f"\n{size}개 요소 정렬 시간 비교:")
        data = list(range(size))
        random.shuffle(data)
        
        for name, sort_func in algorithms:
            data_copy = data.copy()
            start_time = time.time()
            sort_func(data_copy)
            end_time = time.time()
            
            # 정렬 결과 확인
            is_sorted = all(data_copy[i] <= data_copy[i+1] for i in range(len(data_copy)-1))
            
            print(f"{name}: {(end_time - start_time):.6f}초 {'✅' if is_sorted else '❌'}")

def main():
    """모든 자료구조 및 알고리즘 테스트 실행"""
    print_header("파이썬 자료구조 및 알고리즘 테스트")
    
    # 자료구조 테스트
    data_structures = [
        ("스택", "stack"),
        ("큐", "queue"),
        ("연결 리스트", "linked_list"),
        ("이진 트리", "binary_tree"),
        ("해시 테이블", "hash_table")
    ]
    
    for name, module in data_structures:
        test_data_structure(name, module)
    
    # 탐색 알고리즘 테스트
    search_algorithms = [
        ("선형 탐색", "linear_search"),
        ("이진 탐색", "binary_search"),
        ("깊이 우선 탐색", "dfs"),
        ("너비 우선 탐색", "bfs")
    ]
    
    for name, module in search_algorithms:
        test_search_algorithm(name, module)
    
    # 정렬 알고리즘 테스트
    sort_algorithms = [
        ("버블 정렬", "bubble_sort"),
        ("선택 정렬", "selection_sort"),
        ("삽입 정렬", "insertion_sort"),
        ("퀵 정렬", "quick_sort"),
        ("병합 정렬", "merge_sort"),
        ("힙 정렬", "heap_sort")
    ]
    
    for name, module in sort_algorithms:
        test_sort_algorithm(name, module)
    
    # 정렬 알고리즘 성능 비교
    compare_sorting_algorithms()

if __name__ == "__main__":
    main()
