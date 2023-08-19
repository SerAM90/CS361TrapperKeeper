import tkinter
import tkinter as tk
import TrapperKeepPasswordGen as PasswordGenFunc
from tkinter import *
from PIL import ImageTk, Image
import os
import pathlib

window = tk.Tk()
window.wm_title('TrapperKeeper')

window.geometry("400x700")

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
Below code is for the canvas background photo utilized
'''

bg = "images\PSBFallout_resized.jpg"
current_dir = pathlib.Path(__file__).parent.resolve()
bg_path = os.path.join(current_dir, bg)
bg_photo = ImageTk.PhotoImage(Image.open(bg_path))

my_canvas = tk.Canvas(window, width=394, height=700)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg_photo, anchor="nw")


'''
Labels and instructions below
'''

password_output = tk.Label(text='', background="black",fg="orange")
password_output_window = my_canvas.create_window(10,465,anchor="nw",window=password_output)


intro = my_canvas.create_text(120,10,anchor="nw", text='Welcome to Trapper Keeper!', fill="orange")
instructions = my_canvas.create_text(10,30,anchor="nw", fill="orange", text='Instructions: TrapperKeeper is a local random password generator!\n'
                             'You may select the different checkbox options to customize your \npassword experience! '
                             'Input how many characters you would \nlike your password to contain: you can pick from 10-30 characters.\n'
                             'Once you have decided your password length press "Generate Password" \nto create your random password.'
                             ' If you are happy with your generated \npassword, you may press the "Copy Password" to use your password!')


'''
Checkbox creation and assets located below
'''
include_digits = tk.BooleanVar() # Bools for checkbox selection
include_special = tk.BooleanVar()

#Images uses for checkbox
positive_image = PhotoImage( file=os.path.join(current_dir, "images\\thumbsup.png"))
negative_image = ImageTk.PhotoImage(Image.open(os.path.join(current_dir, "images\\ANGRY.jpg")))

includeDigits_checkbox = tk.Checkbutton(window, onvalue=True, offvalue=False, command='digits', variable=include_digits, indicatoron=False, selectimage=positive_image, image=negative_image)
specialchar_checkbox = tk.Checkbutton(window, onvalue=True, offvalue=False, command='special', variable=include_special,indicatoron=False, selectimage=positive_image, image=negative_image)

include_digits_label = tk.Label(text="Include Digits", background="black", fg="orange")
include_digits_label_window = my_canvas.create_window(52,158,anchor="nw",window=include_digits_label)
include_digits_window = my_canvas.create_window(10,150, anchor="nw",window=includeDigits_checkbox)

'''
Window labels and text boxes below to provide backgrounds and coloring to assets
'''
special_char_window = my_canvas.create_window(10,195,anchor="nw", window=specialchar_checkbox)
special_char_text = tkinter.Label(text="Include Special Characters", background="black",fg="orange")
special_char_text_window = my_canvas.create_window(52,202,anchor="nw",window=special_char_text)

password_length_label = tk.Label(window, text="Enter a password length between 10-30: ",background="black",fg="orange")
password_length_label_window = my_canvas.create_window(10,235,anchor="nw",window=password_length_label)
password_length_entry = tk.Entry(window, width=3)
password_length_window = my_canvas.create_window(235,235,anchor="nw",window=password_length_entry)



'''
GUI Buttons code located below
'''

generate_password_button = tk.Button(
    text="Generate Password",
    width=25,
    height=5,
    bg="black",
    fg="orange",
    command=lambda: get_password(password_length_entry))
generate_password_window = my_canvas.create_window(10,265, anchor="nw",window=generate_password_button)

copy_button = tk.Button(
    text="Copy Password",
    width=25,
    height=5,
    bg="black",
    fg="orange",
    command=copy_password)
copy_button_window = my_canvas.create_window(10,365,anchor="nw",window=copy_button)

window.mainloop()
