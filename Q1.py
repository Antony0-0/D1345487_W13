import tkinter as tk
from tkinter import messagebox

users = {
    "Antony": "1111",
    "Dennis": "2222",
    "Terry": "3333"
}

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users and users[username] == password:
        messagebox.showinfo("成功", "登入成功！")
        login_window.destroy()
        start_game()
    else:
        messagebox.showerror("錯誤", "使用者名稱或密碼不正確！")

def start_game():
    global player, buttons
    player = 0 
    buttons = [[None for _ in range(3)] for _ in range(3)]

    game_window = tk.Tk()
    game_window.title("Tic Tac Toe")
    game_window.geometry("300x300")
    game_window.grid_rowconfigure(0, weight=1)
    game_window.grid_rowconfigure(1, weight=1)
    game_window.grid_rowconfigure(2, weight=1)
    game_window.grid_columnconfigure(0, weight=1)
    game_window.grid_columnconfigure(1, weight=1)
    game_window.grid_columnconfigure(2, weight=1)

    def btn_click(row, col):
        global player
        btn = buttons[row][col]
        if btn['text'] == "":
            btn['text'] = "X" if player else "O"
            player = 1 - player
            btn['state'] = tk.DISABLED
            check_winner()

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] and buttons[row][0]['text'] != "":
                declare_winner(buttons[row][0]['text'])
                return

        for col in range(3):
            if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] and buttons[0][col]['text'] != "":
                declare_winner(buttons[0][col]['text'])
                return

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] and buttons[0][0]['text'] != "":
            declare_winner(buttons[0][0]['text'])
            return
        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] and buttons[0][2]['text'] != "":
            declare_winner(buttons[0][2]['text'])
            return

        if all(buttons[row][col]['text'] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo("遊戲結束", "平手！")
            reset_game()

    def declare_winner(winner):
        messagebox.showinfo("遊戲結束", f"玩家 {winner} 獲勝！")
        reset_game()

    def reset_game():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(text="", state=tk.NORMAL)
        global player
        player = 0

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(game_window, text="", font=('Arial', 20), command=lambda r=row, c=col: btn_click(r, c))
            buttons[row][col].grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    game_window.mainloop()

login_window = tk.Tk()
login_window.title("登入")

tk.Label(login_window, text="使用者名稱：").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(login_window, text="密碼：").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(login_window, text="登入", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

login_window.mainloop()