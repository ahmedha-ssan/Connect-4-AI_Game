import tkinter as tk
from game import main

selected_difficulty = 0
selected_algorithm = 0

algorithm_buttons = []
difficulty_buttons = []

def select_algorithm(value):
    global selected_algorithm
    selected_algorithm = value
    reset_button_colors(algorithm_buttons)
    if value == 1:
        button_minmax.config(bg="red")
    elif value == 2:
        button_alphabeta.config(bg="red")
    
def select_difficulty(value):
    global selected_difficulty
    selected_difficulty = value
    reset_button_colors(difficulty_buttons)
    if value == 1:
        button_easy.config(bg="red")
    elif value == 2:
        button_medium.config(bg="red")
    elif value == 3:
        button_hard.config(bg="red")


def reset_button_colors(button_list):
    for button in button_list:
        button.config(bg="blue")


def get_input():
    a = selected_algorithm
    b = selected_difficulty
    main(a, b)


window = tk.Tk()
window.title("AI project")
window.geometry("800x500")
window.configure(bg="black")

label_algorithm = tk.Label(window, text="Select an algorithm:", bg="black", fg="white",font=20)
label_algorithm.grid(row=0, column=0, pady=(20, 10), sticky="W")

button_minmax = tk.Button(window, text="Min-Max", command=lambda: select_algorithm(1), bg="blue", fg="white", bd=0, relief=tk.SOLID, borderwidth=1, highlightthickness=0, width=15, height=2, highlightcolor="black")
button_minmax.grid(row=0, column=1, pady=(20, 10), padx=(10, 10))
algorithm_buttons.append(button_minmax)

button_alphabeta = tk.Button(window, text="Alpha-Beta", command=lambda: select_algorithm(2), bg="blue", fg="white", bd=0, relief=tk.SOLID, borderwidth=1, highlightthickness=0, width=15, height=2, highlightcolor="black")
button_alphabeta.grid(row=0, column=2, pady=(20, 10), padx=(10, 10))
algorithm_buttons.append(button_alphabeta)

label_difficulty = tk.Label(window, text="Select a difficulty level:", bg="black", fg="white")
label_difficulty.grid(row=1, column=0, pady=(10, 10), sticky="W")

button_easy = tk.Button(window, text="Easy", command=lambda: select_difficulty(1), bg="blue", fg="white", bd=0, relief=tk.SOLID, borderwidth=1, highlightthickness=0, width=15, height=2, highlightcolor="black")
button_easy.grid(row=1, column=1, pady=(10, 10), padx=(10, 10))
difficulty_buttons.append(button_easy)

button_medium = tk.Button(window, text="Medium", command=lambda: select_difficulty(2), bg="blue", fg="white", bd=0, relief=tk.SOLID, borderwidth=1, highlightthickness=0, width=15, height=2, highlightcolor="black")
button_medium.grid(row=1, column=2, pady=(10, 10), padx=(10, 10))
difficulty_buttons.append(button_medium)

button_hard = tk.Button(window, text="Hard", command=lambda: select_difficulty(3), bg="blue", fg="white", bd=0, relief=tk.SOLID, borderwidth=1, highlightthickness=0, width=15, height=2, highlightcolor="black")
button_hard.grid(row=1, column=3, pady=(10, 10), padx=(10, 10))
difficulty_buttons.append(button_hard)

button_get_input = tk.Button(window, text="Make game", command=get_input, bg="blue", fg="white", bd=0, relief=tk.SOLID, borderwidth=1, highlightthickness=0, width=30, height=2, highlightcolor="black")
button_get_input.grid(row=2, column=0, columnspan=4, pady=(20, 0))

label_sum = tk.Label(window, text="", bg="black", fg="white")
label_product = tk.Label(window, text="", bg="black", fg="white")
label_sum.grid(row=3, column=0, pady=(20, 10))
label_product.grid(row=4, column=0, pady=(10, 20))

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"+{x}+{y}")

window.mainloop()
