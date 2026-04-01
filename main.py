import tkinter
from multiprocessing import Value
import tkinter as tk
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "*", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4
"""
color_light_gray = (225, 225, 225)
color_light_red = (255, 0, 0)
color_light_green = (0, 255, 0)
color_light_blue = (0, 0, 255)
color_light_yellow = (255, 255, 0)
"""


#window
window = tk.Tk()
window.title("calculator")
window.resizable(width=False, height=False)

frame = tk.Frame(window)
label = tk.Label(frame, text="0", font=("Arial", 20), fg="blue", bg="black", anchor="e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we" )

def button_clicked(value):
    pass

for row in range(row_count):
    for column in range(column_count):
        # noinspection PyUnresolvedReferences
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 20), fg="yellow", bg="white",
                                width=column_count-1, height=1, command=lambda value=value:button_clicked(value))
        button.grid(row=row+1, column=column)

        if value in top_symbols:
            tk.Button(fg="blue", bg="black")
        elif value in right_symbols:
            tk.Button(fg="blue" ,bg="black")
        else:
            tk.Button(bg="gray", fg="blue")
        button.grid(row=row+1, column=column)

frame.pack()
#A+B A-B A*B A/B
A = 0
operator = None
B = None

def clear_all():
    global A, B, operator
    A ="0"
    operator = None
    B = None



def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator
    if value in right_symbols:
        pass
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        if value == "+/-":
            pass
        if value == "%":
            pass
    else:
        if value == ".":
            if value not in label["text"]:
                 label["text"] += value
        elif value in "0123456789":
            if label["text"] =="0":
                label["text"] = value # replace 0 when the user tries to type 0 i.e 05 to display just 5
            else:
                label["text"] += value


# center the window
window.update() #update the calculator window with the new size of dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2)-(window_width / 2))
window_y = int((screen_height / 2)-(window_height / 2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()


