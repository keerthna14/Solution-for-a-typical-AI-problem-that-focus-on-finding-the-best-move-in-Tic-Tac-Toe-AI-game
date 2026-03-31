import tkinter as tk
from tkinter import messagebox

# Window setup
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.configure(bg="#1e1e2f")

board = ["_"] * 9
buttons = []

AI, USER = "O", "X"

wins = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

# Check winner
def is_win(b, p):
    return any(b[a] == b[b2] == b[c] == p for a, b2, c in wins)

# Get winning cells
def get_winning_cells(b, p):
    for a, b2, c in wins:
        if b[a] == b[b2] == b[c] == p:
            return (a, b2, c)
    return None

# Draw check
def is_draw():
    return "_" not in board

# AI move
def ai_move():
    best = None

    for i in range(9):
        if board[i] == "_":
            temp = board.copy()
            temp[i] = AI
            if is_win(temp, AI):
                best = i
                break

    if best is None:
        for i in range(9):
            if board[i] == "_":
                temp = board.copy()
                temp[i] = USER
                if is_win(temp, USER):
                    best = i
                    break

    if best is None:
        for p in [4,0,2,6,8,1,3,5,7]:
            if board[p] == "_":
                best = p
                break

    board[best] = AI
    buttons[best].config(text=AI, fg="#ff4d4d", state="disabled")

# Animate winning cells
def highlight_win(cells):
    for i in cells:
        buttons[i].config(bg="#00ffcc")

# Button click
def on_click(i):
    if board[i] == "_":
        board[i] = USER
        buttons[i].config(text=USER, fg="#00bfff", state="disabled")

        win_cells = get_winning_cells(board, USER)
        if win_cells:
            highlight_win(win_cells)
            root.after(300, lambda: (messagebox.showinfo("Game Over", "You Win! 🎉"), reset()))
            return

        if is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset()
            return

        ai_move()

        win_cells = get_winning_cells(board, AI)
        if win_cells:
            highlight_win(win_cells)
            root.after(300, lambda: (messagebox.showinfo("Game Over", "AI Wins 🤖"), reset()))
            return

        if is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset()

# Reset game
def reset():
    global board
    board = ["_"] * 9
    for btn in buttons:
        btn.config(text="", state="normal", bg="#2c2c3e")

# Hover effects
def on_enter(e):
    if e.widget["state"] == "normal":
        e.widget.config(bg="#3a3a5a")

def on_leave(e):
    if e.widget["state"] == "normal":
        e.widget.config(bg="#2c2c3e")

# Create buttons
for i in range(9):
    btn = tk.Button(root, text="", width=6, height=3,
                    font=("Arial", 20, "bold"),
                    bg="#2c2c3e", fg="white",
                    activebackground="#444",
                    command=lambda i=i: on_click(i))
    
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    buttons.append(btn)

# Reset button
tk.Button(root, text="Reset", command=reset,
          bg="#ffcc00", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=3, sticky="we", pady=10)

root.mainloop()
