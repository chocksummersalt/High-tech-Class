a = list(input("수식을 입력해주세요: "))  # 예: 3+5*2

stack = []
result = []

# 연산자 우선순위 정의
p = {'+': 1, '-': 1, '*': 2, '%': 2}

for i in a:
    if i not in "+-*%":
        result.append(i)
    else:
        while stack and p.get(stack[-1]) >= p[i]:
            result.append(stack.pop())
        stack.append(i)

# 스택에 남은 연산자들을 결과에 추가
while stack:
    result.append(stack.pop())

print("후위 표기식:", ''.join(result))
