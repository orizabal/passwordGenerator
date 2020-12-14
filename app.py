import random
import string
import inquirer

# set default password requirements
length = 5
includeLower = True
includeUpper = True
includeNums = True
inludeSymbols = True

questions = {
    'changeDefault': [inquirer.List(
        'changeDefault',
        message='Would you like to change these defaults?',
        choices=['Yes', 'No']
    )],
    'selectDefault': [inquirer.List(
        'selectDefault',
        message='Which setting would you like to modify?: ',
        choices=['Password Length', 'Inclues Uppercase', 'Includes Lowercase', 'Includes Numbers', 'Includes Symbols']
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
    'By default, your password will be 5 characters in length and will include lowercase letters, uppercase letters, numbers, and symbols. \n'
)

changeInput = inquirer.prompt(questions['changeDefault'])

while changeAnother['changeAnother'] == 'Yes':

    def passLength():
        length = int(input('How long would you like your password to be?: '))

    def inclUpper():
        userChangeUpper = inquirer.prompt(questions['changeUpper'])
        if (userChangeUpper['changeUpper'] == 'Yes'):
            includeUpper = True
        else:
            includeUpper = False

    def inclLower():
        userChangeLower = inquirer.prompt(questions['changeLower'])
        if (userChangeLower['changeLower'] == 'Yes'):
            includeLower = True
        else:
            includeLower = False

    def inclNum():
        userChangeNumber = inquirer.prompt(questions['changeNumber'])
        if (userChangeNumber['changeNumber'] == 'Yes'):
            includeNums = True
        else:
            includeNums = False

    def inclSymb():
        userChangeSymbol = inquirer.prompt(questions['changeSymbol'])
        if (userChangeSymbol['changeSymbol'] == 'Yes'):
            includeSymbols = True
        else:
            includeSymbols = False

    changeDefaults = {
        'Password Length': passLength,
        'Inclues Uppercase': inclUpper,
        'Includes Lowercase': inclLower,
        'Includes Numbers': inclNum,
        'Includes Symbols': inclSymb
    }

    selectDefaultInput = inquirer.prompt(questions['selectDefault'])

    changeDefaults[selectDefaultInput['selectDefault']]()

    changeAnother = inquirer.prompt(questions['changeAnother'])





