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

color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey="#505050"
color_orange="#FF9500"
color_white= "white"



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
        button = tkinter.Button(frame, text=value, font=("Arial", 20), fg="green", bg="white",
                                width=column_count-1, height=1, command=lambda value=value:button_clicked(value))
        button.grid(row=row+1, column=column)

        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_grey)
        elif value in right_symbols:
            button.config(foreground=color_white ,background=color_orange)
        else:
            tk.Button(bg="gray", fg="white")
        button.grid(row=row+1, column=column)

frame.pack()
#A+B A-B A*B A/B
A = 0
operator = None
B = None

def clear_all():
    global A, operator, B
    A ="0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)[:12]

                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)[:12]

                elif operator == "*":
                    label["text"] = remove_zero_decimal(numA * numB)[:12]

                elif operator == "÷":
                    if numB != 0:
                        label["text"] = remove_zero_decimal(numA / numB)[:12]
                    else:
                        label["text"] = "Error"
                
                A = label["text"]
                operator = None
                B = None

        elif value in "+-*÷":
            if label["text"] != "Error":
                A = label["text"]
            label["text"] = "0"
            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)[:12]

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)[:12]

    else:
        if value == "√":
            try:
                import math
                num = float(label["text"])
                if num >= 0:
                    result = math.sqrt(num)
                    label["text"] = remove_zero_decimal(result)[:12]
                else:
                    label["text"] = "Error"
            except ValueError:
                label["text"] = "Error"
        elif value == ".":
            if value not in label["text"] and len(label["text"]) < 12:
                 label["text"] += value
        elif value in "0123456789":
            if len(label["text"]) < 12:
                if label["text"] =="0" or label["text"] == "Error":
                    label["text"] = value # replace 0 when the user tries to type 0 ie 05 to display just 5
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
