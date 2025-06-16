"""
큐(Queue) 구현
- FIFO(First-In-First-Out) 원칙을 따르는 자료구조
- 주요 연산: enqueue(삽입), dequeue(제거), peek(조회), is_empty(비어있는지 확인)
- 시간 복잡도: 모든 연산 O(1)
"""

class Queue:
    def __init__(self):
        """큐 초기화"""
        self.items = []
    
    def enqueue(self, item):
        """큐에 요소 추가 (뒤쪽)"""
        self.items.append(item)
    
    def dequeue(self):
        """큐에서 요소 제거 및 반환 (앞쪽)"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        """큐의 맨 앞 요소 반환 (제거하지 않음)"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """큐가 비어있는지 확인"""
        return len(self.items) == 0
    
    def size(self):
        """큐의 크기 반환"""
        return len(self.items)
    
    def __str__(self):
        """큐의 문자열 표현 반환"""
        return str(self.items)


# 사용 예제
if __name__ == "__main__":
    queue = Queue()
    
    print("큐 연산 예제:")
    print(f"큐가 비어있나요? {queue.is_empty()}")
    
    print("\n요소 추가: 10, 20, 30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"현재 큐: {queue}")
    
    print(f"\n큐 크기: {queue.size()}")
    print(f"맨 앞 요소 확인: {queue.peek()}")
    
    print(f"\n요소 제거: {queue.dequeue()}")
    print(f"요소 제거 후 큐: {queue}")
    
    print(f"\n요소 제거: {queue.dequeue()}")
    print(f"요소 제거: {queue.dequeue()}")
    print(f"모든 요소 제거 후 큐: {queue}")
    
    print(f"\n큐가 비어있나요? {queue.is_empty()}")
    
    # 참고: 이 구현은 dequeue 연산이 O(n)이므로 실제로는 collections.deque를 사용하는 것이 더 효율적입니다.
    print("\n파이썬 collections 모듈의 deque를 사용한 효율적인 큐 구현 예시:")
    from collections import deque
    
    efficient_queue = deque()
    efficient_queue.append(10)  # enqueue
    efficient_queue.append(20)
    efficient_queue.append(30)
    print(f"deque로 구현한 큐: {efficient_queue}")
    print(f"요소 제거: {efficient_queue.popleft()}")  # dequeue - O(1) 시간 복잡도
    print(f"제거 후 큐: {efficient_queue}")
