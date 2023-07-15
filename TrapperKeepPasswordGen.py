import secrets

print('TrapperKeeper! You personal password generator!')
print('Instructions: TrapperKeeper is a local password generator that allows you to generate a random 10, or 20 character password.')
print('You will select if you would like a 10, or 20 character password. Then you will be guided on decided between Alphabetical, numerical, or mixed characters.')
print('You will have the option to add "special characters" as well.')

password_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #Set the alphabetical chars for password
password_numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #Set the numerical chars for password
password_special = ['!', '@', '-', '_', '&', '#', '%'] #list of special chars that can be used

mixed_password = password_alpha + password_numerical #To create a mixed password

password_twenty = 20
password_ten = 10
generated_password = ' '

while True:
    user_input = input('Please enter "10" for a 10 character password, or "20" for a 20 character password:')

    if user_input == '20':
        for index in range(password_twenty):
            generated_password += ''.join(secrets.choice(password_alpha))
        print(generated_password)


    if user_input == '10':
        for index in range(password_ten):
            generated_password += ''.join(secrets.choice(password_numerical))
        print(generated_password)
    generated_password = ' '