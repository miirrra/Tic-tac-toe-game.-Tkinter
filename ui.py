# файл ui.py
import tkinter as tk
from tkinter import messagebox

from game_logic import make_move, check_winner, switch_player


class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")

        # игровое поле
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        # создаём кнопки
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            btn = tk.Button(
                self.root,
                text=" ",
                font=("Arial", 24),
                bg= "red",
                fg="black",
                width=5,
                height=2,
                command=lambda pos=i: self.on_button_click(pos)
            )
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_button_click(self, pos):
        if make_move(self.board, pos, self.current_player):
            self.buttons[pos].config(text=self.current_player)

            result = check_winner(self.board)
            if result:
                if result == "Draw":
                    messagebox.showinfo("Игра окончена", "Ничья!")
                else:
                    messagebox.showinfo("Игра окончена", f"Победил: {result}")
                self.reset_game()
                return

            self.current_player = switch_player(self.current_player)

        else:
            messagebox.showwarning("Ход невозможен", "Клетка уже занята!")

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        for btn in self.buttons:
            btn.config(text=" ")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
