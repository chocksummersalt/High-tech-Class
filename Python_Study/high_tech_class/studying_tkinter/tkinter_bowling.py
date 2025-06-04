import tkinter # GUI 만드는 라이브러리
import random 

# 게임 시작 버튼을 누르면 함수 실행.
def start_game():
    # 매번 게임을 새로 시작할 때마다 결과를 저장할 리스트를 초기화
    frame_results =[]
    hap=[]
    for frame in range(1, 11):
        first = random.randint(0, 10)

        #스트라이크
        if first == 10:
            result_text = f"{frame}프레임: 스트라이크"
            frame_results.append(result_text)
            continue 

        second = random.randint(0, 10 - first)

        # 스페어
        if first + second == 10:
            # 결과 리스트에 스페어 표시
            result_text = f"{frame}프레임: {first} /"
            frame_results.append(result_text)
        # 아무것도 아닐 때
        else:
            # 결과 리스트에 두 투구의 점수를 추가.
            result_text = f"{frame}프레임: {first}, {second}"
            frame_results.append(result_text)

 
    display = "\n".join(frame_results)
    label.config(text=display)

#메뉴의 종료를 누르면 이 함수 실행
def close():
    window.quit() # tkinter 메인 루프 종료
    window.destroy() # 창 닫기

# GUI 설정
# 메인
window = tkinter.Tk()
window.title("성민이의 볼링 게임") # 창 제목 설정
window.geometry("640x400") # 창 크기 설정 
window.resizable(False, False) # 창 크기 조절 못하게 막기

# 메뉴바 만들기
menubar = tkinter.Menu(window) # 메뉴바 객체 생성

# 게임 메뉴 만들기
menu_game = tkinter.Menu(menubar, tearoff=0) # 게임 메뉴 생성
menu_game.add_command(label="게임 시작", command=start_game)

menu_game.add_separator() # 구분선 추가
# 게임 메뉴에 종료 옵션 추가, 누르면 close함수 실행
menu_game.add_command(label="종료", command=close)
# 메뉴바에 게임 메뉴 추가
menubar.add_cascade(label="게임 메뉴", menu=menu_game)

# 창에 메뉴바 설정
window.config(menu=menubar)
# 결과 표시될 레이블(글자 표시판) 만들기
label = tkinter.Label(window,fg="blue",height=10, text="🎳 볼링 게임 시작! 🎳", width=50,relief="solid")
label.pack()#이거 붙여줘야 실행됨
button = tkinter.Button(window, text="게임 시작!", width=20, command=start_game) # 누르면 실행될 함수
button.pack() #이것도 마찬가지. 그리드에 생성에 관련된 매서드인듯.

window.mainloop() 
