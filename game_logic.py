# файл game_logic.py 
board = [" " for _ in range(9)]

def make_move(board, position, symbol):
    if board[position] == " ":
        board[position] = symbol
        return True
    return False


def check_winner(board):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),  # линии
        (0,3,6),(1,4,7),(2,5,8),  # столбцы
        (0,4,8),(2,4,6)           # диагонали
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]  # X или O

    if " " not in board:
        return "Draw"

    return None

def switch_player(current):
    return "O" if current == "X" else "X"
