"""
Играта „Живот“ (на английски: Game of Life, Conway's Game of Life) е популярна игра
с нула на брой играчи, измислена през 1970 година от Джон Хортън Конуей,
която се явява най-известният пример за клетъчен автомат.
Пространството на играта е (крайна или безкрайна) двумерна решетка от квадратни клетки,
всяка от които може да се намира в едно от общо две възможни състояния: жива или мъртва.
Всяка клетка от решетката взаимодейства с осемте си съседа, т.е. клетките разположени
в съседство от нея по хоризонтал, вертикал и диагонал. На итеративен принцип,
състоянието на всяка клетка в решетката запазва или променя състоянието си в зависимост
от предварително зададен списък от правила.

Играта е пример за способности като възникване (самопораждане) и самоорганизация.
С това как сложни структури се генерират от прилагането на прости правила тя
представлява интерес за физици, биолози, икономисти, математици, философи и учени
от други научни направления.

Правила на играта:

    - Всяка жива клетка с по-малко от две живи съседни клетки умира (от самота).
    - Всяка жива клетка с повече от три живи съседни клетки умира (от пренаселеност).
    - Всяка жива клетка с две или три живи съседни клетки остава жива и на следващата итерация.
    - Всяка мъртва клетка с точно три живи съседни клетки се превръща в жива клетка.

Началното състояние на полето се разглежда като своеобразен посев. На всяка итерация
(още наричана „генерация“, „поколение“) правилата на системата се прилагат едновременно
към всяка отделна клетка в полето и новите „раждания“ и „смърти“ на клетките се
случват едновременно. По този начин всяка итерация е функция, зависеща само от състоянието
на системата от предходната итерация, и няма елемент на случайност. В този смисъл
играта е за нула играчи: това означава, че развоят ѝ се определя само от началното ѝ състояние,
без да е необходима намеса от човек. Взаимодействието на човека с играта се изчерпва
със задаването на началните стойности на клетките в полето, наблюдението на развитието ѝ и
евентуалното ѝ прекъсване след определен брой итерации.

-------------------------------------------------------------------------------

Решетката ще бъде представене като списък от списъци (виж `board` отдолу).
Клетките ще бъдат представени като числа (0 за мъртва клетка и 1 за жива).

На всяка итерация решетката се рисува.
Селд това от нея се създава решетка за следващото поколение (чрез функцията next_generation).
За целта се използвата функциите next_cell_state, коята определя стойността на
всяка клетка (0 или 1). На нея и е нужен броя живи съседни клетки, които се
изчисляват от функцията alive_cell_neighbours).
"""

import turtle
import math
import time

from conway import next_cell_state

PLAYGROUND_SIDE = 200
CELLS_COUNT_PER_SIDE = 5
CELL_SIDE = PLAYGROUND_SIDE / CELLS_COUNT_PER_SIDE

# Set up screen
window = turtle.Screen()
window.bgcolor('black')
window.tracer(0)

pen = turtle.Turtle()
pen.fillcolor('white')
pen.speed(0)


def drow_cell(x, y):
    pen.setx(x * CELL_SIDE - PLAYGROUND_SIDE / 2)
    pen.sety(-(y * CELL_SIDE - PLAYGROUND_SIDE / 2))
    pen.dot(CELL_SIDE, 'white')


def drow_board(board):
    pen.clear()
    for i in range(CELLS_COUNT_PER_SIDE):
        for j in range(CELLS_COUNT_PER_SIDE):
            cell = board[i + 1][j + 1]
            if cell == 1:
                drow_cell(j, i)


def empty_board(side):
    board = []
    for i in range(side):
        row = []
        for j in range(side):
            row.append(0)
        board.append(row)
    return board


def next_generation(board):
    new_board = empty_board(CELLS_COUNT_PER_SIDE + 2)
    for i in range(1, CELLS_COUNT_PER_SIDE + 1):
        for j in range(1, CELLS_COUNT_PER_SIDE + 1):
            new_board[i][j] = next_cell_state(i, j, board)
    return new_board


# Решетката
# Клетките ще бъдат представени като числа (0 за мъртва клетка и 1 за жива).
# За по лесна реализация на играте границите на решетката (първи и последен
# ред, първа и последна килона) трябва да са мъртви (стойнос 0)
board = [
    [0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,0,1,1,0],
    [0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

play_game = True

def quit_game():
    global play_game
    play_game = False

window.listen()
window.onkey(quit_game, 'q')

while play_game:
    drow_board(board)
    window.update()
    time.sleep(1)
    board = next_generation(board)

window.bye()

