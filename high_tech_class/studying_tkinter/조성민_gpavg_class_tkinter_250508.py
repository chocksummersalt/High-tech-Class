import tkinter 
import random as rd
import os

class Grade:
    def __init__(self, name):
        self.grades = []
        self.name = name

    def get_random_score(self):
        score = rd.randint(0, 100)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def add(self):
        grade_letter = self.get_random_score()
        if grade_letter == "A":
            self.grades.append(4.5)
        elif grade_letter == "B":
            self.grades.append(3.5)
        elif grade_letter == "C":
            self.grades.append(2.5)
        elif grade_letter == "D":
            self.grades.append(1.5)
        else:
            self.grades.append(0.0)

    def avg(self):
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades),2)

def close():
    window.quit()
    window.destroy()

# GUI
window = tkinter.Tk()
window.title("평균내기")
window.geometry("640x400")
window.resizable(False, False)

entry = tkinter.Entry(window) #등급 입력을 시켜서 점수 평균이 나오게 하고싶은데..
entry.pack()

# 배경 이미지
try:
    image = tkinter.PhotoImage(file="background.png")
    label_image = tkinter.Label(window, image=image)
    label_image.image = image
    label_image.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print("이미지를 불러올 수 없습니다")

# 메뉴바
menubar = tkinter.Menu(window)
menu_game = tkinter.Menu(menubar, tearoff=0)
menu_game.add_command(label="시작", command=lambda: show())
menu_game.add_separator()
menu_game.add_command(label="종료", command=close)
menubar.add_cascade(label="메뉴", menu=menu_game)
window.config(menu=menubar)

# 텍스트 라벨
label = tkinter.Label(window, fg="blue", height=10, text="평균을 내볼까요?", width=50, relief="solid")
label.pack()

button = tkinter.Button(window, text="평균내기 시작", width=20, command=lambda: show())
button.pack()

# 객체 생성
student = Grade("조성민")

def show():
    for subject in range(5):  # 5과목 점수 생성
        student.add()
    average = student.avg()
    label.config(text=f"{student.name}의 평균학점: {average}")

window.mainloop()
