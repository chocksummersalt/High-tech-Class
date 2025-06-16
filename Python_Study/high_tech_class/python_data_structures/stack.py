"""
스택(Stack) 구현
- LIFO(Last-In-First-Out) 원칙을 따르는 자료구조
- 주요 연산: push(삽입), pop(제거), peek(조회), is_empty(비어있는지 확인)
- 시간 복잡도: 모든 연산 O(1)
"""

class Stack:
    def __init__(self):
        """스택 초기화"""
        self.items = []
    
    def push(self, item):
        """스택에 요소 추가"""
        self.items.append(item)
    
    def pop(self):
        """스택에서 요소 제거 및 반환"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """스택의 맨 위 요소 반환 (제거하지 않음)"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """스택이 비어있는지 확인"""
        return len(self.items) == 0
    
    def size(self):
        """스택의 크기 반환"""
        return len(self.items)
    
    def __str__(self):
        """스택의 문자열 표현 반환"""
        return str(self.items)


# 사용 예제
if __name__ == "__main__":
    stack = Stack()
    
    print("스택 연산 예제:")
    print(f"스택이 비어있나요? {stack.is_empty()}")
    
    print("\n요소 추가: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"현재 스택: {stack}")
    
    print(f"\n스택 크기: {stack.size()}")
    print(f"맨 위 요소 확인: {stack.peek()}")
    
    print(f"\n요소 제거: {stack.pop()}")
    print(f"요소 제거 후 스택: {stack}")
    
    print(f"\n요소 제거: {stack.pop()}")
    print(f"요소 제거: {stack.pop()}")
    print(f"모든 요소 제거 후 스택: {stack}")
    
    print(f"\n스택이 비어있나요? {stack.is_empty()}")
