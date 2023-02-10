# Игровое поле
board = list(range(1, 10))

print("Первый игрок: Х \t Второй игрок: О")

def style_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)


# Проверка на число
def input_number(player_key):
    active = 0
    while active == 0:
        player_input = input ("Куда поставим: " + player_key + " ?\n")

        try:
            player_input = int(player_input)
        except:
            print("Некорректный ввод, введите число.")
            continue
        if player_input >= 1 and player_input <= 9:
            if str(board[player_input - 1]) not in "XO":
                board[player_input - 1] = player_key
                active += 1
            else:
                print("Клетка занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9")


# Проверка на win комбинации
def check_win(board):
    win_comb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_comb:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

# Main
def main(board):
    win = 0
    while win <= 9:
        style_board(board)
        if win % 2 == 0:
            input_number("X")
        else:
            input_number("O")
        win += 1
        if check_win(board):
            print(check_win(board), "Выиграл!")
            break
        if win == 9:
            print("Ничья!")
            break
    style_board(board)
main(board)

