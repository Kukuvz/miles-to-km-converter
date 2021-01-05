from tkinter import *


def convert():
    miles = float(input_miles.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=110)
window.config(padx=50, pady=20)

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

mil_label = Label(text="Miles")
mil_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
