import tkinter 
import random as rd
import os
class grade:
    def __init__(self, name):
        self.grade = {}
        self.name = name # 학생 이름
        self.hakjum = 0 # 학점 초기화
    def ABC(self):
        hakjum = rd.randint(0, 100)
        if hakjum >= 90:
            return "A"
        elif hakjum >= 80:
            return "B"
        elif hakjum >= 70:
            return "C"
        elif hakjum >= 60:
            return "D"
        else:
            return "F"
        

    def add(self, grade):
        self.hakjum = self.ABC()
        if self.hakjum == "A":
            grade += 4.5
        elif self.hakjum == "B":
            grade += 3.5
        elif self.hakjum == "C":
            grade += 2.5
        elif self.hakjum == "D":
            grade += 1.5
        else:
            grade += 0.0
        self.grade[self.name] = grade # 딕셔너리 형태로 저장

    def avg(self):
        total = 0
        for i in self.grade.values():
            total += i
        average = total / len(self.grade)
        return average



        
def close():
    window.quit() # tkinter 메인 루프 종료
    window.destroy() # 창 닫기

# GUI 설정
# 메인
window = tkinter.Tk()
window.title("평균내기") # 창 제목 설정
window.geometry("640x400") # 창 크기 설정 
window.resizable(False, False) # 창 크기 조절 못하게 막기

entry = tkinter.Entry(window) # Entry 위젯 생성
entry.pack() # Entry 위젯 배치

# 배경 이미지 설정
image = tkinter.PhotoImage(file="C:/Users/AISW-006/workspace/webstudy/sungmin_webdev_250418/image/background.png") # 배경 이미지 설정
label_image = tkinter.Label(window, image=image) # 배경 이미지 레이블 생성
label_image.place(x=0, y=0, relwidth=1, relheight=1) # 배경 이미지 레이블 크기 설정
print(os.path.dirname(os.path.realpath(__file__))) # 현재 파일 경로 확인
# 메뉴바 만들기
menubar = tkinter.Menu(window) # 메뉴바 객체 생성


menu_game = tkinter.Menu(menubar, tearoff=0) #메뉴 생성
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

student = grade("조성민민") # grade 클래스 객체 생성
def show():
    average=student.avg() # 객체 불러오기
    label.config(text=f"평균학점: {average}") # 레이블에 평균학점 표시

    # 메인 루프 시작

window.mainloop() 
