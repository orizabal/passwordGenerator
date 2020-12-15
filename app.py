import random
import string
import inquirer

# set default password requirements
length = 8
lower = True
upper = True
numbers = True
symbols = True

questions = {
    'changeDefault': [inquirer.List(
        'changeDefault',
        message='Would you like to change these defaults?',
        choices=['Yes', 'No']
    )],
    'selectDefault': [inquirer.List(
        'selectDefault',
        message='Which setting would you like to modify?: ',
        choices=['Password Length', 'Includes Uppercase', 'Includes Lowercase', 'Includes Numbers', 'Includes Symbols']
    )],
    'changeAnother': [inquirer.List(
        'changeAnother',
        message='Would you like to change another setting?',
        choices=['Yes', 'No']
    )],
    'changeUpper': [inquirer.List(
        'changeUpper',
        message='Would you like your password to include uppercase letters?',
        choices=['Yes', 'No']
    )],
    'changeLower': [inquirer.List(
        'changeLower',
        message='Would you like your password to include lowercase letters?',
        choices=['Yes', 'No']
    )],
    'changeNumber': [inquirer.List(
        'changeNumber',
        message='Would you like your password to include numbers?',
        choices=['Yes', 'No']
    )],
    'changeSymbol': [inquirer.List(
        'changeSymbol',
        message='Would you like your password to include symbols?',
        choices=['Yes', 'No']
    )],
}

changeAnother = {
    'changeAnother': 'Yes'
}

# tell user the default requirements
print(
    'Welcome to the Password Generator! \n\n' +
    'By default, your password will be 8 characters in length and will include' +
    ' lowercase letters, uppercase letters, numbers, and symbols. \n'
)

changeInput = inquirer.prompt(questions['changeDefault'])

if changeInput['changeDefault'] == 'Yes':
    while changeAnother['changeAnother'] == 'Yes':

        def passLength():
            global length
            length = int(input('How long would you like your password to be?: '))

        def inclUpper():
            global upper
            upper = True if inquirer.prompt(questions['changeUpper']) == 'Yes' else False

        def inclLower():
            global lower
            lower = True if inquirer.prompt(questions['changeLower']) == 'Yes' else False

        def inclNum():
            global numbers
            numbers = True if inquirer.prompt(questions['changeNumber']) == 'Yes' else False

        def inclSymb():
            global symbols
            symbols = True if inquirer.prompt(questions['changeSymbol']) == 'Yes' else False

        changeDefaults = {
            'Password Length': passLength,
            'Includes Uppercase': inclUpper,
            'Includes Lowercase': inclLower,
            'Includes Numbers': inclNum,
            'Includes Symbols': inclSymb
        }

        selectDefaultInput = inquirer.prompt(questions['selectDefault'])

        changeDefaults[selectDefaultInput['selectDefault']]()

        changeAnother = inquirer.prompt(questions['changeAnother'])

password_characters = (
    (string.ascii_letters.upper() if upper else '') +
    (string.ascii_letters.lower() if lower else '') +
    (string.digits if numbers else '') +
    (string.punctuation if symbols else '')
)

password = ''.join(random.choice(password_characters) for x in range(0, length))

print('Your password is: \n\n' + password + '\n\nThank you for using the Password Generator! \n')


