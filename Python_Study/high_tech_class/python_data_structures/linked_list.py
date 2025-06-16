"""
연결 리스트(Linked List) 구현
- 각 노드가 데이터와 다음 노드에 대한 참조를 가지는 선형 자료구조
- 주요 연산: append(추가), insert(삽입), remove(제거), search(검색)
- 시간 복잡도: 검색/삽입/삭제 O(n), 맨 앞/뒤 삽입 O(1)
"""

class Node:
    def __init__(self, data):
        """노드 초기화"""
        self.data = data
        self.next = None
    
    def __str__(self):
        """노드의 문자열 표현 반환"""
        return str(self.data)


class LinkedList:
    def __init__(self):
        """연결 리스트 초기화"""
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """연결 리스트가 비어있는지 확인"""
        return self.head is None
    
    def append(self, data):
        """연결 리스트 끝에 노드 추가"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """연결 리스트 앞에 노드 추가"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
    
    def insert(self, data, position):
        """지정된 위치에 노드 삽입"""
        if position < 0 or position > self.size:
            raise IndexError("위치가 범위를 벗어났습니다.")
        
        if position == 0:
            self.prepend(data)
            return
        
        if position == self.size:
            self.append(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # position-1 위치까지 이동
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def remove(self, data):
        """데이터를 가진 첫 번째 노드 제거"""
        if self.is_empty():
            return False
        
        # 헤드 노드를 제거하는 경우
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            
            # 리스트가 비어있게 된 경우
            if self.head is None:
                self.tail = None
            
            return True
        
        # 다른 노드를 제거하는 경우
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        # 데이터를 찾은 경우
        if current.next:
            # 테일 노드를 제거하는 경우
            if current.next == self.tail:
                self.tail = current
            
            current.next = current.next.next
            self.size -= 1
            return True
        
        return False
    
    def search(self, data):
        """데이터를 가진 노드의 인덱스 반환, 없으면 -1 반환"""
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, position):
        """지정된 위치의 노드 데이터 반환"""
        if position < 0 or position >= self.size:
            raise IndexError("위치가 범위를 벗어났습니다.")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def __len__(self):
        """연결 리스트의 크기 반환"""
        return self.size
    
    def __str__(self):
        """연결 리스트의 문자열 표현 반환"""
        if self.is_empty():
            return "[]"
        
        result = []
        current = self.head
        
        while current:
            result.append(str(current.data))
            current = current.next
        
        return "[" + " -> ".join(result) + "]"


# 사용 예제
if __name__ == "__main__":
    linked_list = LinkedList()
    
    print("연결 리스트 연산 예제:")
    print(f"연결 리스트가 비어있나요? {linked_list.is_empty()}")
    
    print("\n요소 추가: 10, 20, 30")
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print(f"현재 연결 리스트: {linked_list}")
    
    print("\n맨 앞에 요소 추가: 5")
    linked_list.prepend(5)
    print(f"현재 연결 리스트: {linked_list}")
    
    print("\n중간에 요소 삽입: 위치 2에 15 삽입")
    linked_list.insert(15, 2)
    print(f"현재 연결 리스트: {linked_list}")
    
    print(f"\n연결 리스트 크기: {len(linked_list)}")
    
    print(f"\n20의 위치 검색: {linked_list.search(20)}")
    print(f"40의 위치 검색: {linked_list.search(40)}")
    
    print(f"\n위치 3의 요소 가져오기: {linked_list.get(3)}")
    
    print("\n요소 제거: 15")
    linked_list.remove(15)
    print(f"제거 후 연결 리스트: {linked_list}")
    
    print("\n요소 제거: 5 (맨 앞)")
    linked_list.remove(5)
    print(f"제거 후 연결 리스트: {linked_list}")
    
    print("\n요소 제거: 30 (맨 뒤)")
    linked_list.remove(30)
    print(f"제거 후 연결 리스트: {linked_list}")
