from pygame import *
import math


window = display.set_mode((640, 640))
display.set_caption('Chess')
font.init()


def drawBackground():
    rectArr = []
    for i in range(8):
        for j in range(4):
            rectArr.append(Rect((j * 160 + (i % 2) * 80, i * 80, 80, 80)))
    draw.rect(window, (179, 159, 122), (0, 0, 640, 640))
    for r in rectArr:
        draw.rect(window, (128, 64, 48), r)


def drawPieces():
    y = 0
    for brd in Board:
        x = 0
        for b in brd:
            if Board[y][x] != '.':
                window.blit(transform.scale(image.load('img\\' + Board[y][x] + '.png'), (70, 70)), (x * 80 + 5, y * 80 + 5))
            x += 1
        y += 1


Board = [['R1', 'H1', 'B1', 'Q1', 'K1', 'B1', 'H1', 'R1'],
         ['p1', 'p1', 'p1', 'p1', 'p1', 'p1', 'p1', 'p1'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['P0', 'P0', 'P0', 'P0', 'P0', 'P0', 'P0', 'P0'],
         ['R0', 'H0', 'B0', 'Q0', 'K0', 'B0', 'H0', 'R0']]

AttackDict = {
    'R': [[0, 1], [1, 0], [0, -1], [-1, 0], 1],
    'B': [[1, 1], [-1, -1], [1, -1], [-1, 1], 1],
    'Q': [[1, 1], [-1, -1], [1, -1], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], 1],
    'H': [[1, 2], [2, 1], [-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, -2], [2, -1], 0],
    'P': [[-1, -1], [1, -1], 0],
    'p': [[-1, 1], [1, 1], 0],
    'K': [[1, 1], [-1, -1], [1, -1], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], 0]
}


def checkMoves(x, y):
    global moves
    moves = []
    B = Board[y][x]
    for shift in AttackDict[B[0]][0:-1]:
        pos = [x, y]
        for i in range(AttackDict[B[0]][-1] * 6 + 1):
            pos[0] += shift[0]
            pos[1] += shift[1]
            if pos[0] > 7 or pos[0] < 0 or pos[1] > 7 or pos[1] < 0:
                break
            if Board[pos[1]][pos[0]] != '.':
                if Board[pos[1]][pos[0]][1] != Board[y][x][1]:
                    moves.append([pos[0], pos[1]])
                    break
                else:
                    break
            elif B[0] != 'p' and B[0] != 'P':
                moves.append([pos[0], pos[1]])

    if B[0] == 'P':
        pos = [x, y]
        for i in range((y == 6) + 1):
            pos[1] -= 1
            if pos[1] < 0:
                break
            if Board[pos[1]][pos[0]] != '.':
                break
            moves.append([pos[0], pos[1]])

    if B[0] == 'p':
        pos = [x, y]
        for i in range((y == 1) + 1):
            pos[1] += 1
            if pos[1] > 7:
                break
            if Board[pos[1]][pos[0]] != '.':
                break
            moves.append([pos[0], pos[1]])


    ForDeletion = []
    Board[y][x] = '.'
    for m in moves:
        remember = Board[m[1]][m[0]]
        Board[m[1]][m[0]] = B
        if checkShah(B[1]):
            ForDeletion.append(m)
        Board[m[1]][m[0]] = remember
    Board[y][x] = B
    for Del in ForDeletion:
        moves.remove(Del)

    if Board[y][x] == 'K0':
        global flagL0, flagR0
        if Board[7][0:5] == ['R0', '.', '.', '.', 'K0'] and flagL0:
            Board[7][2], Board[7][3] = 'K0', 'K0'
            if checkShah('0') == 0:
                moves.append([2, 7])
            Board[7][2], Board[7][3] = '.', '.'

        if Board[7][4:8] == ['K0', '.', '.', 'R0'] and flagR0:
            Board[7][5], Board[7][6] = 'K0', 'K0'
            if checkShah('0') == 0:
                moves.append([6, 7])
            Board[7][5], Board[7][6] = '.', '.'

    if Board[y][x] == 'K1':
        global flagL1, flagR1
        if Board[0][0:5] == ['R1', '.', '.', '.', 'K1'] and flagL1:
            Board[0][2], Board[0][3] = 'K1', 'K1'
            if checkShah('1') == 0:
                moves.append([2, 0])
            Board[0][2], Board[0][3] = '.', '.'

        if Board[0][4:8] == ['K1', '.', '.', 'R1'] and flagR1:
            Board[0][5], Board[0][6] = 'K1', 'K1'
            if checkShah('1') == 0:
                moves.append([6, 0])
            Board[0][5], Board[0][6] = '.', '.'


def checkShah(B_W):
    y = 0
    for Brd in Board:
        x = 0
        for B in Brd:
            if B != '.':
                if B[1] != B_W:
                    for shift in AttackDict[B[0]][0:-1]:
                        pos = [x, y]
                        for i in range(AttackDict[B[0]][-1] * 6 + 1):
                            pos[0] += shift[0]
                            pos[1] += shift[1]
                            if pos[0] > 7 or pos[0] < 0 or pos[1] > 7 or pos[1] < 0:
                                break
                            if Board[pos[1]][pos[0]] != '.':
                                if Board[pos[1]][pos[0]] != 'K' + B_W:
                                    break
                                else:
                                    return True
            x += 1
        y += 1
    return False


def checkMate(b_w):
    global moves
    y = 0
    for brd in Board:
        x = 0
        for b in brd:
            if b[-1] == b_w:
                checkMoves(x, y)
                if len(moves) > 0:
                    moves = []
                    return 0
            x += 1
        y += 1
    if checkShah(b_w):
        moves = []
        return 1
    else:
        moves = []
        return 2

flagL0, flagR0 = True, True
flagL1, flagR1 = True, True
moves = []
drawBackground()
drawPieces()
turn = 0
Game = 1
check = 0

def game():
    global turn, Game, flagL0, flagR0, flagL1, flagR1, moves, check
    while Game:
        if Board[0].count('P0') and turn == 1:
            turn = -1
            pawnX = Board[0].index('P0')
            window.blit(transform.scale(image.load('img\\' + 'Q0.png'), (40, 40)), (pawnX * 80, 0))
            window.blit(transform.scale(image.load('img\\' + 'B0.png'), (40, 40)), (40 + pawnX * 80, 0))
            window.blit(transform.scale(image.load('img\\' + 'R0.png'), (40, 40)), (pawnX * 80, 40))
            window.blit(transform.scale(image.load('img\\' + 'H0.png'), (40, 40)), (40 + pawnX * 80, 40))

        if Board[7].count('p1') and turn == 0:
            turn = -2
            pawnX = Board[7].index('p1')
            window.blit(transform.scale(image.load('img\\' + 'Q1.png'), (40, 40)), (pawnX * 80, 560))
            window.blit(transform.scale(image.load('img\\' + 'B1.png'), (40, 40)), (40 + pawnX * 80, 560))
            window.blit(transform.scale(image.load('img\\' + 'R1.png'), (40, 40)), (pawnX * 80, 600))
            window.blit(transform.scale(image.load('img\\' + 'H1.png'), (40, 40)), (40 + pawnX * 80, 600))

        for e in event.get():
            if e.type == QUIT:
                Game = 0

            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if turn == -1:
                    x, y = e.pos
                    if pawnX + 1 > x / 80 >= pawnX and y < 80:
                        x %= 80
                        if 40 > x >= 0 and 40 > y >= 0:
                            Board[0][pawnX] = 'Q0'
                        elif 40 > x >= 0 and 80 > y >= 40:
                            Board[0][pawnX] = 'R0'
                        elif 80 > x >= 40 and 40 > y >= 0:
                            Board[0][pawnX] = 'B0'
                        elif 80 > x >= 40 and 80 > y >= 40:
                            Board[0][pawnX] = 'H0'
                        turn = 1
                        drawBackground()
                        drawPieces()
                        check = checkMate('1')
                        if check == 1:
                            window.blit(font.SysFont(None, 30).render('WHITE WON', False, (100, 100, 100)), (260, 310))
                        if check == 2:
                            window.blit(font.SysFont(None, 30).render('DRAW', False, (100, 100, 100)), (260, 310))

                if turn == -2:
                    x, y = e.pos
                    if pawnX + 1 > x / 80 >= pawnX and y >= 560:
                        x %= 80
                        if 40 > x >= 0 and 600 > y >= 560:
                            Board[7][pawnX] = 'Q1'
                        elif 40 > x >= 0 and 640 > y >= 600:
                            Board[7][pawnX] = 'R1'
                        elif 80 > x >= 40 and 600 > y >= 560:
                            Board[7][pawnX] = 'B1'
                        elif 80 > x >= 40 and 640 > y >= 600:
                            Board[7][pawnX] = 'H1'
                        turn = 0
                        drawBackground()
                        drawPieces()
                        check = checkMate('0')
                        if check == 1:
                            window.blit(font.SysFont(None, 30).render('BLACK WON', False, (255, 255, 255)), (260, 310))
                        if check == 2:
                            window.blit(font.SysFont(None, 30).render('DRAW', False, (255, 255, 255)), (260, 310))
                else:
                    x, y = e.pos
                    x, y = math.floor(x / 80), math.floor(y / 80)
                    if Board[y][x] != '.':
                        if Board[y][x][1] == str(turn):
                            checkMoves(x, y)
                            cage = [x, y]
                            for m in moves:
                                draw.circle(window, (200, 200, 200), (m[0] * 80 + 40, m[1] * 80 + 40), 10)

            if e.type == MOUSEBUTTONUP and e.button == 1 and turn != -1 and turn != -2:
                x, y = e.pos
                x, y = math.floor(x / 80), math.floor(y / 80)
                if moves.count([x, y]):
                    Board[y][x] = Board[cage[1]][cage[0]]
                    Board[cage[1]][cage[0]] = '.'

                    if cage == [4, 7] and Board[y][x] == 'K0':
                        if [x, y] == [2, 7]:
                            Board[7][0] = '.'
                            Board[7][3] = 'R0'
                        if [x, y] == [6, 7]:
                            Board[7][7] = '.'
                            Board[7][5] = 'R0'
                    if cage == [4, 0] and Board[y][x] == 'K1':
                        if [x, y] == [2, 0]:
                            Board[0][0] = '.'
                            Board[0][3] = 'R1'
                        if [x, y] == [6, 0]:
                            Board[0][7] = '.'
                            Board[0][5] = 'R1'

                    if Board[7][0] != 'R0': flagL0 = False
                    if Board[7][7] != 'R0': flagR0 = False
                    if Board[7][4] != 'K0': flagL0 = False; flagR0 = False
                    if Board[0][0] != 'R1': flagL1 = False
                    if Board[0][7] != 'R1': flagR1 = False
                    if Board[0][4] != 'K1': flagL1 = False; flagR1 = False

                    turn = 1 - turn
                    check = checkMate(str(turn))
                    if check == 1:
                        drawBackground()
                        drawPieces()
                        if turn == 0:
                            window.blit(font.SysFont(None, 30).render('BLACK WON', False, (255, 255, 255)), (260, 310))
                        if turn == 1:
                            if check == 1:
                                window.blit(font.SysFont(None, 30).render('WHITE WON', False, (255, 255, 255)),
                                            (260, 310))
                    if check == 2:
                        window.blit(font.SysFont(None, 30).render('DRAW', False, (255, 255, 255)), (260, 310))
                    moves = []
                if check == 0:
                    drawBackground()
                    drawPieces()
                moves = []
        display.update()