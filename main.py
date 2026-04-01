import tkinter
from multiprocessing import Value

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

color_light_gray = (225, 225, 225)
color_light_red = (255, 0, 0)
color_light_green = (0, 255, 0)
color_light_blue = (0, 0, 255)
color_light_yellow = (255, 255, 0)

#window
window = tkinter.Tk()
window.title("calculator")
window.resizable(width=False, height=False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 20), fg="white", bg="black")

label.grid(row=0, column=0)

def button_clicked(value):
    pass

for row in range(row_count):
    for column in range(column_count):
        # noinspection PyUnresolvedReferences
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 20), fg="white", bg="black",
                                width=column_count-1, height=1, command=lambda value=value:button_clicked(value))
        button.grid(row=row+1, column=column)
frame.pack()

window.mainloop()


