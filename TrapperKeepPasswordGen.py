import secrets
import string

password_alpha = string.ascii_letters
password_numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #Set the numerical chars for password
password_special = ['!', '@', '-', '_', '&', '#', '%'] #list of special chars that can be used




def generate_password(password_length):
    generated_password = ' '
    for index in range(password_length):
        generated_password += ''.join(secrets.choice(password_alpha))
    return generated_password
