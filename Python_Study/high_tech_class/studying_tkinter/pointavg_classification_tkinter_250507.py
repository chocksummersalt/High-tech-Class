import tkinter 
import random as rd

class gpa:
    def __init__(self):
        self.subject = []


    def avg(self, 머릿수=5):
        self.subject = [] # 과목 리스트 초기화 //주의하자 초기화
        for i in range(머릿수):
            self.score = rd.randint(0,100)            
            self.subject.append(self.score)
        total = sum(self.subject)
        aveg = total/len(self.subject)
        print(f"{머릿수}명의 평균학점:", aveg)
        return aveg

student = gpa() # 객체 생성

def close():
    window.quit() # tkinter 메인 루프 종료
    window.destroy() # 창 닫기

# GUI 설정
# 메인
window = tkinter.Tk()
window.title("평균내기") # 창 제목 설정
window.geometry("640x400") # 창 크기 설정 
window.resizable(False, False) # 창 크기 조절 못하게 막기

# 메뉴바 만들기
menubar = tkinter.Menu(window) # 메뉴바 객체 생성


menu_game = tkinter.Menu(menubar, tearoff=0) # 게임 메뉴 생성
menu_game.add_command(label="시작", command= lambda: show())

menu_game.add_separator() # 구분선 추가
# 누르면 close함수 실행
menu_game.add_command(label="종료", command=close)

menubar.add_cascade(label="메뉴", menu=menu_game)

# 창에 메뉴바 설정
window.config(menu=menubar)
# 결과 표시될 레이블(글자 표시판) 만들기
label = tkinter.Label(window,fg="blue",height=10, text="평균을 내볼까요?", width=50,relief="solid")
label.pack()#이거 붙여줘야 실행됨
button = tkinter.Button(window, text="평균내기 시작", width=20, command=lambda: show()) # 누르면 실행될 함수
button.pack() #이것도 마찬가지. 그리드에 생성에 관련된 매서드인듯.

def show():
    average=student.avg() # 객체 불러오기
    label.config(text=f"평균학점: {average}") # 레이블에 평균학점 표시

    # 메인 루프 시작

window.mainloop() 

"""import tkinter g
import random as rd

class GPA:
    def __init__(self):
        self.subject = []

    def avg(self, 머릿수=5):
        self.subject = []  # 매번 새로운 점수 리스트를 시작
        for _ in range(머릿수):
            score = rd.randint(0, 100)
            self.subject.append(score)
        
        total = sum(self.subject)  # 총점
        average = total / len(self.subject)  # 평균 계산
        print(f"{머릿수}명의 평균학점:", average)
        return average  # GUI에서 결과를 표시하기 위해 반환

# GUI 설정
window = tkinter.Tk()
window.title("평균내기")  # 창 제목 설정
window.geometry("640x400")  # 창 크기 설정 
window.resizable(False, False)  # 창 크기 조절 못하게 막기

# 객체 생성
student = GPA()

def close():
    window.quit()  # tkinter 메인 루프 종료
    window.destroy()  # 창 닫기

# 메뉴바 만들기
menubar = tkinter.Menu(window)  # 메뉴바 객체 생성

menu_game = tkinter.Menu(menubar, tearoff=0)  # 게임 메뉴 생성
menu_game.add_command(label="시작", command=lambda: student.avg())  # `self`를 `student`로 수정

menu_game.add_separator()  # 구분선 추가
menu_game.add_command(label="종료", command=close)

menubar.add_cascade(label="메뉴", menu=menu_game)

# 창에 메뉴바 설정
window.config(menu=menubar)

# 결과 표시될 레이블(글자 표시판) 만들기
label = tkinter.Label(window, fg="blue", height=10, text="평균을 내볼까요?", width=50, relief="solid")
label.pack()  # 레이블 창에 붙이기

# 버튼 클릭 시 평균 내기 시작
def start_avg():
    average = student.avg()  # 평균 계산
    label.config(text=f"평균학점: {average:.2f}")  # 레이블에 평균 표시

button = tkinter.Button(window, text="평균내기 시작", width=20, command=start_avg)  # 버튼 클릭 시 `start_avg` 함수 실행
button.pack()  # 버튼 창에 붙이기

# 메인 루프 시작
window.mainloop()
"""