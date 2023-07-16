import tkinter as tk
import TrapperKeepPasswordGen as PasswordGenFunc
window = tk.Tk()
window.wm_title('TrapperKeeper')

def generate_password(password_length):
    password_generated = PasswordGenFunc.generate_password(password_length)
    password_output["text"] = password_generated



password_output = tk.Label(text='')
instructions = tk.Label(text='Instructions: TrapperKeeper is a random password generator! \n'
                             'Push the "Generate 10 character Password", or "Generate 20 character Password" '
                             'to create a password of 10 or 20 characters in length!')

instructions.pack()




ten_button = tk.Button(
    text="Generate 10 Character Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: generate_password(10))

twenty_button = tk.Button(
    text="Generate 20 Character Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: generate_password(20))

ten_button.pack()
twenty_button.pack()
password_output.pack()
window.mainloop()
