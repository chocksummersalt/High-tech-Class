maze = [['1','1','1','1','1','1'],
        ['e','0','0','0','0','0'],
        ['1','0','1','0','1','1'],
        ['1','1','1','0','0','x'],
        ['1','1','1','0','1','1'],
        ['1','1','1','1','1','1']]

maze_size = 6

found = False  # 탈출지점을 찾았는지 확인
for i in range(maze_size):
    for j in range(maze_size):
        if maze[i][j] == 'x':
            print(f"({i},{j}) 위치에서 탈출구 x 발견~")
            found = True
            break
    if found:
        break