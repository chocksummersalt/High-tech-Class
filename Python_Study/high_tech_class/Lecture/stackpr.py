insert = input("수식을 입력하세요") #입력받고
stack = [] #넣어둘 스택 만들고
output = []
num = ["0","1", "2", "3", "4","5","6","7","8","9"] #숫자 인풋 리스트
연산자 = ["*","-","+","/"] #연산자 검출할 리스트
우선순위 = {"*": 2, "/": 2, "+": 1, "-": 1}

for i in insert: #검출 할때까지 반복하기
    if i in 연산자: #연산자 먼저 있으면
        stack.append(i) #스택에 저장
    elif i in num: #다음 숫자 있으면 숫자 빼내기
        while stack and stack[-1] in 연산자 and 우선순위[stack[-1]] >= 우선순위[i]:
            output.append(stack.pop())
            stack.append(i)

while stack:
    output.append(stack.pop())

print("후위표기식", ''.join(output))

        


