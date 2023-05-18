import tkinter as tk
from game import main



def get_input():
  
    a = int(entry_a.get())
    b = int(entry_b.get())
    main(a, b)

window = tk.Tk()
window.title("AI project")
window.geometry("800x500")
window.title("Integer Input")

label_a = tk.Label(window, text="for min max enter 1,for alpha beta enter 2:")
label_b = tk.Label(window, text="Enter  1 for easy or  2 for medium or 3 for hard:")
label_sum = tk.Label(window, text="")
label_product = tk.Label(window, text="")

entry_a = tk.Entry(window)
entry_b = tk.Entry(window)

button_get_input = tk.Button(window, text="make game", command=get_input)

window.rowconfigure(1, minsize=20)  # Adds 20 pixels of vertical space after row 0
window.rowconfigure(3, minsize=40)

label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_b.grid(row=2, column=0)
entry_b.grid(row=2, column=1)
button_get_input.grid(row=4, column=0)
label_sum.grid(row=3, column=0)
label_product.grid(row=4, column=0)

window.mainloop()