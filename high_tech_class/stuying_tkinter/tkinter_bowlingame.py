import tkinter

window = tkinter.Tk()
window.title("sungmin's bowling game")
window.geometry("640x400+100+100")
window.resizable(True,True)

label=tkinter.Label(window, text="볼링게임 250501",width=10,height=5,fg="red",relief="solid")
label.pack()

window.mainloop()
