import tkinter
import random


window = tkinter.Tk()
window.title("sungmin's bowling game")
window.geometry("640x400+100+100")
window.resizable(True,True)


count = 0

class bowlingame_start:
    def __init__(self):
    
        self.rolls = []

    def roll(self, pins):
        pins = 10
        self.roll = pins - random.randint(0,10)



    def close():
        window.quit()
        window.destroy()

menubar=tkinter.Menu(window)

menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="게임결과 보기", command=bowlingame_start)
menu_1.add_separator()
menu_1.add_command(label="메뉴 닫기", command=close)
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

menu_2=tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_radiobutton(label="하위메뉴 2-1", state="disable")
menubar.add_cascade(label="상위 메뉴 2",menu=menu_2)

label=tkinter.Label(window, text="볼링게임 250501",width=50,height=10,fg="red",relief="solid")
label.pack()

button = tkinter.Button(window,text="시작시켜봐" ,overrelief="solid",width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()


window.config(menu=menubar)
window.mainloop()

print("window close")