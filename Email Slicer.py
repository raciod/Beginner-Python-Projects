import re

def email_slicer():
    email = input('Enter your email: ')
    # Variables
    user_name = re.findall(r"[A-z0-9]+@", email)[0][:-1]
    mail_name = re.findall(r"@\w+", email)[0][1:]
    domaine = re.findall(r"\.\w+", email)[0][1:]

    # Print the result
    print('Your email slice is:')
    print(f'User name: {user_name}')
    print(f'Mail name: {mail_name}')
    print(f'Domaine: {domaine}')

email_slicer()
