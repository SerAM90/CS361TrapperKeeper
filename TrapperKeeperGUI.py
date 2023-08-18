import tkinter as tk
import TrapperKeepPasswordGen as PasswordGenFunc


window = tk.Tk()
window.wm_title('TrapperKeeper')


def get_password(password_length):
    password_generated = PasswordGenFunc.generate_password(password_length, include_digits.get(), include_special.get())
    password_output["text"] = password_generated

def copy_password():
    generated_password = password_output["text"]
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    window.update()
    print("Password copied to clipboard!")



password_output = tk.Label(text='')
intro = tk.Label(text='Hello!, and Welcome to TrapperKeeper! A local password generator without encryption that allows you to generate a random password.')
instructions = tk.Label(text='Instructions: TrapperKeeper is a random password generator! \n'
                             'You may select the different checkbox options to customize your password experience! \n'
                             'Push the "Generate 10 character Password", or "Generate 20 character Password" '
                             'to create a password of 10 or 20 characters in length!')
intro.pack()
instructions.pack()

include_digits = tk.BooleanVar()
include_special = tk.BooleanVar()

includeDigits_checkbox = tk.Checkbutton(window, text='Include Digits', onvalue=True, offvalue=False, command='digits', variable=include_digits)
includeDigits_checkbox.pack()

specialchar_checkbox = tk.Checkbutton(window, text='Include Special Characters', onvalue=True, offvalue=False, command='special', variable=include_special)
specialchar_checkbox.pack()


ten_button = tk.Button(
    text="Generate 10 Character Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: get_password(10))

twenty_button = tk.Button(
    text="Generate 20 Character Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: get_password(20))

copy_button = tk.Button(
    text="Copy Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=copy_password)


ten_button.pack()
twenty_button.pack()
copy_button.pack()

password_output.pack()
window.mainloop()
