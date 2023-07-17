import tkinter as tk
import TrapperKeepPasswordGen as PasswordGenFunc
window = tk.Tk()
window.wm_title('TrapperKeeper')

def generate_password(password_length):
    password_generated = PasswordGenFunc.generate_password(password_length)
    password_output["text"] = password_generated



password_output = tk.Label(text='')
intro = tk.Label(text='Hello!, and Welcome to TrapperKeeper! A local password generator without encryption that allows you to generate a random password.')
instructions = tk.Label(text='Instructions: TrapperKeeper is a random password generator! \n'
                             'You may select the different checkbox options to customize your password experience! \n'
                             'Push the "Generate 10 character Password", or "Generate 20 character Password" '
                             'to create a password of 10 or 20 characters in length!')
intro.pack()
instructions.pack()

twenty_checkbox = tk.Checkbutton(window, text='20 Character Password', onvalue=1, offvalue=0, command='20')
twenty_checkbox.pack()

ten_checkbox = tk.Checkbutton(window, text='10 Character Password', onvalue=1, offvalue=0, command='10')
ten_checkbox.pack()

mixedchar_checkbox = tk.Checkbutton(window, text='Mixed Character Password', onvalue=1, offvalue=0, command='mixed')
mixedchar_checkbox.pack()

specialchar_checkbox = tk.Checkbutton(window, text='Include Special Characters in Password', onvalue=1, offvalue=0, command='special')
specialchar_checkbox.pack()


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

copy_button = tk.Button(
    text="Copy Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command='')

newpassword_button = tk.Button(
    text="Create New Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command='')

ten_button.pack()
twenty_button.pack()
copy_button.pack()
newpassword_button.pack()
password_output.pack()
window.mainloop()
