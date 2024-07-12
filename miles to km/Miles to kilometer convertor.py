from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometers_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=60, pady=20)

window.geometry("300x100")  

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=0, row=0)  

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

kilometers_label = Label(text="KM")
kilometers_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()