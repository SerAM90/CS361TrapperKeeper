import tkinter as tk
import TrapperKeepPasswordGen as PasswordGenFunc
window = tk.Tk()

def generate_password(password_length):
    password_generated = PasswordGenFunc.generate_password(password_length)
    password_output["text"] = password_generated



password_output = tk.Label(text='')
label = tk.Label(text='Python rock!')

label.pack()
password_output.pack()



ten_button = tk.Button(
    text="Generate 10 character Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: generate_password(10))

twenty_button = tk.Button(
    text="Generate 20 character Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: generate_password(20))

ten_button.pack()
twenty_button.pack()

window.mainloop()
