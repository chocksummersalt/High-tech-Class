"""
이진 트리(Binary Tree) 구현
- 각 노드가 최대 두 개의 자식 노드를 가질 수 있는 트리 구조
- 주요 연산: 삽입, 검색, 순회(전위, 중위, 후위)
- 시간 복잡도: 균형 트리에서 검색/삽입/삭제 O(log n), 불균형 트리에서 최악 O(n)
"""

class TreeNode:
    def __init__(self, data):
        """트리 노드 초기화"""
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        """노드의 문자열 표현 반환"""
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        """이진 검색 트리 초기화"""
        self.root = None
    
    def is_empty(self):
        """트리가 비어있는지 확인"""
        return self.root is None
    
    def insert(self, data):
        """트리에 새 노드 삽입"""
        if self.is_empty():
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """재귀적으로 노드 삽입"""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data):
        """트리에서 데이터 검색"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """재귀적으로 데이터 검색"""
        if node is None:
            return False
        
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def preorder_traversal(self):
        """전위 순회 (루트 -> 왼쪽 -> 오른쪽)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """재귀적 전위 순회"""
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def inorder_traversal(self):
        """중위 순회 (왼쪽 -> 루트 -> 오른쪽)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """재귀적 중위 순회"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """후위 순회 (왼쪽 -> 오른쪽 -> 루트)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """재귀적 후위 순회"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def delete(self, data):
        """트리에서 노드 삭제"""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """재귀적으로 노드 삭제"""
        if node is None:
            return None
        
        # 삭제할 노드 찾기
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # 자식이 없거나 하나만 있는 경우
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # 두 자식이 모두 있는 경우
            # 오른쪽 서브트리에서 가장 작은 값을 찾아 대체
            node.data = self._find_min_value(node.right)
            node.right = self._delete_recursive(node.right, node.data)
        
        return node
    
    def _find_min_value(self, node):
        """노드의 서브트리에서 최소값 찾기"""
        current = node
        while current.left:
            current = current.left
        return current.data
    
    def height(self):
        """트리의 높이 계산"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """재귀적으로 높이 계산"""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return max(left_height, right_height) + 1


# 사용 예제
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    print("이진 검색 트리 연산 예제:")
    print(f"트리가 비어있나요? {bst.is_empty()}")
    
    print("\n요소 삽입: 50, 30, 70, 20, 40, 60, 80")
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
    
    print("\n트리 순회 결과:")
    print(f"전위 순회 (Preorder): {bst.preorder_traversal()}")
    print(f"중위 순회 (Inorder): {bst.inorder_traversal()}")
    print(f"후위 순회 (Postorder): {bst.postorder_traversal()}")
    
    print(f"\n트리 높이: {bst.height()}")
    
    print(f"\n40이 트리에 있나요? {bst.search(40)}")
    print(f"90이 트리에 있나요? {bst.search(90)}")
    
    print("\n요소 삭제: 30")
    bst.delete(30)
    print(f"삭제 후 중위 순회: {bst.inorder_traversal()}")
    
    print("\n요소 삭제: 50 (루트)")
    bst.delete(50)
    print(f"삭제 후 중위 순회: {bst.inorder_traversal()}")
