from board import *

def print_board():
    print('  A   B   C   D   E   F   G   H')
    for number in '12345678':
        print(number, end=' ')
        for symbol in 'ABCDEFGH':
            for figure in figures:
                if symbol + number == ''.join(list(map(str, figure.position))):
                    print(figure.getName(), end=' ')
                    break

            else:
                print('[ ]', end=' ')

        print('\n')


def game():
    while True:
        print_board()
        current_move = input('Enter position of figure (X0): ')
        for figure in figures:
            if current_move == ''.join(list(map(str, figure.position))):
                move_position = input('Enter move position (X0): ')
                if figure.isMoveValid(move_position) == True:
                    choice = input('Are u sure? (y/n): ')
                    if choice == 'y':
                        figure.move(move_position)
                break
        else:
            ...



if __name__ == '__main__':
    game()