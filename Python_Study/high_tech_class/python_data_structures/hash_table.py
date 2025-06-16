"""
해시 테이블(Hash Table) 구현
- 키-값 쌍을 저장하는 자료구조로, 해시 함수를 사용하여 키를 배열 인덱스로 변환
- 주요 연산: 삽입, 검색, 삭제
- 시간 복잡도: 평균적으로 삽입/검색/삭제 O(1), 최악의 경우 O(n)
"""

class HashTable:
    def __init__(self, size=10):
        """해시 테이블 초기화"""
        self.size = size
        self.table = [[] for _ in range(size)]  # 체이닝 방식으로 충돌 처리
        self.count = 0
    
    def _hash_function(self, key):
        """해시 함수: 키를 해시 테이블 인덱스로 변환"""
        if isinstance(key, str):
            # 문자열 키의 경우 각 문자의 아스키 값을 합산
            hash_value = 0
            for char in key:
                hash_value += ord(char)
            return hash_value % self.size
        else:
            # 숫자 키의 경우 단순히 모듈로 연산
            return key % self.size
    
    def insert(self, key, value):
        """키-값 쌍 삽입"""
        index = self._hash_function(key)
        
        # 이미 키가 존재하는지 확인
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # 값 업데이트
                return
        
        # 새 키-값 쌍 추가
        self.table[index].append((key, value))
        self.count += 1
        
        # 로드 팩터가 0.7을 초과하면 리사이징
        if self.count / self.size > 0.7:
            self._resize()
    
    def get(self, key):
        """키에 해당하는 값 검색"""
        index = self._hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        # 키를 찾지 못한 경우
        raise KeyError(f"키 '{key}'를 찾을 수 없습니다.")
    
    def remove(self, key):
        """키-값 쌍 삭제"""
        index = self._hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
        
        # 키를 찾지 못한 경우
        return False
    
    def contains(self, key):
        """키가 존재하는지 확인"""
        index = self._hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return True
        
        return False
    
    def _resize(self):
        """해시 테이블 크기 조정"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        # 기존 항목들을 새 테이블에 재삽입
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def keys(self):
        """모든 키 반환"""
        all_keys = []
        for bucket in self.table:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys
    
    def values(self):
        """모든 값 반환"""
        all_values = []
        for bucket in self.table:
            for _, value in bucket:
                all_values.append(value)
        return all_values
    
    def items(self):
        """모든 키-값 쌍 반환"""
        all_items = []
        for bucket in self.table:
            all_items.extend(bucket)
        return all_items
    
    def __len__(self):
        """해시 테이블에 저장된 항목 수 반환"""
        return self.count
    
    def __str__(self):
        """해시 테이블의 문자열 표현 반환"""
        result = "{\n"
        for bucket in self.table:
            for key, value in bucket:
                result += f"  {key}: {value},\n"
        result += "}"
        return result


# 사용 예제
if __name__ == "__main__":
    hash_table = HashTable()
    
    print("해시 테이블 연산 예제:")
    
    print("\n키-값 쌍 삽입:")
    hash_table.insert("name", "홍길동")
    hash_table.insert("age", 30)
    hash_table.insert("email", "hong@example.com")
    hash_table.insert("phone", "010-1234-5678")
    print(hash_table)
    
    print(f"\n항목 수: {len(hash_table)}")
    
    print("\n키 검색:")
    print(f"'name' 키의 값: {hash_table.get('name')}")
    print(f"'age' 키의 값: {hash_table.get('age')}")
    
    print("\n키 존재 여부 확인:")
    print(f"'email' 키가 존재하나요? {hash_table.contains('email')}")
    print(f"'address' 키가 존재하나요? {hash_table.contains('address')}")
    
    print("\n키 업데이트:")
    hash_table.insert("age", 31)  # 기존 키 업데이트
    print(f"'age' 키의 새 값: {hash_table.get('age')}")
    
    print("\n키 삭제:")
    hash_table.remove("phone")
    print(f"삭제 후 해시 테이블: {hash_table}")
    
    print("\n모든 키:", hash_table.keys())
    print("모든 값:", hash_table.values())
    print("모든 항목:", hash_table.items())
