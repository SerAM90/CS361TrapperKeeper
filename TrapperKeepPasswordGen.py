import secrets
import string
import PwdClient as ClientValidation

password_alpha = string.ascii_letters
password_numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #Set the numerical chars for password
password_special = ['!', '@', '-', '_', '&', '#', '%'] #list of special chars that can be used


def generate_password(password_length, include_numerical, include_special):
    valid_password = False
    generated_password = ''

    password_list = password_alpha
    if include_numerical:
        space_str = ''.join(password_numerical)
        password_list = password_list + space_str
    if include_special:
        space_str = ''.join(password_special)
        password_list = password_list + space_str

    while valid_password is False:
        generated_password = ''
        for index in range(password_length):
            generated_password += ''.join(secrets.choice(password_list))
        password_dictionary = {
        'password': generated_password,
        # 'password': 'wvFf75dIqMgfMO8s5mBH',
        'upper_length': password_length,
        'lower_length': password_length,
        'digit': include_numerical,
        'uppercase': True,
        'lowercase': True,
        'symbol': include_special
        }
        valid_password = ClientValidation.validate_password(password_dictionary)
        print(password_dictionary)
        print('Was the password valid?: ', valid_password)
    return generated_password


