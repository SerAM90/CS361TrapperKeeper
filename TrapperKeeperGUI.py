import tkinter as tk
import TrapperKeepPasswordGen as PasswordGenFunc
from tkinter import *
from PIL import ImageTk, Image


window = tk.Tk()
window.wm_title('TrapperKeeper')

'''
Functions below for GUI to TrapperKeepPasswordGen interactions - Getting the password, and Copy button for the GUI
'''
def get_password(password_length):

    try:
        password_length = int(password_length_entry.get())
        if 10 <= password_length <= 30:
            password_generated = PasswordGenFunc.generate_password(password_length, include_digits.get(), include_special.get())
            password_output["text"] = password_generated
        else:
            password_output["text"] = "Password length must be between 10 and 30 characters!"
    except ValueError:
        password_output["text"] = "Please enter a valid integer for your password length!"


def copy_password():
    generated_password = password_output["text"]
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    window.update()
    print("Password copied to clipboard!")

'''
Labels and instructions below
'''
password_output = tk.Label(text='')
intro = tk.Label(text='Hello!, and Welcome to TrapperKeeper! A local password generator without encryption that allows you to generate a random password.')
instructions = tk.Label(text='Instructions: TrapperKeeper is a random password generator! \n'
                             'You may select the different checkbox options to customize your password experience! \n'
                             'Input how many characters you would like your password to contain: you can pick from 10-30 characters \n'
                             'Once you have decided your password length press "Generate Password" to create your random password \n'
                             'If you are happy with your generated password, you may press the "Copy Password" to use your password!')

intro.pack()
instructions.pack()

include_digits = tk.BooleanVar()
include_special = tk.BooleanVar()

includeDigits_checkbox = tk.Checkbutton(window, text='Include Digits', onvalue=True, offvalue=False, command='digits', variable=include_digits)
includeDigits_checkbox.pack()

specialchar_checkbox = tk.Checkbutton(window, text='Include Special Characters', onvalue=True, offvalue=False, command='special', variable=include_special)
specialchar_checkbox.pack()

password_length_label = tk.Label(window, text="Enter a password length between 10-30: ")
password_length_label.pack()

password_length_entry = tk.Entry(window)
password_length_entry.pack()


'''
Checkboxes located below
'''

copy_button = tk.Button(
    text="Copy Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=copy_password)

generate_password_button = tk.Button(
    text="Generate Password",
    width=25,
    height=5,
    bg="black",
    fg="green",
    command=lambda: get_password(password_length_entry))

'''
GUI button packs()
'''
generate_password_button.pack()
copy_button.pack()


password_output.pack()
window.mainloop()
