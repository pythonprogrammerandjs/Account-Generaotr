name = 'Enter a name in this variable'

print('Welcome to ' + name + ', lets get you all set up, create you an acount, with a password and a username!')

setup_username = input('Enter a username: ')
username = ''
username = setup_username

setup_password = input('Enter a password: ')
password = ''
password = setup_password

if password == username:
    print('Password and username cannot match.')

retype_password = input('Retype your password: ')
if retype_password == password:
    print('Successfully made account: ' + username)

else:
    print('Passwords do not match.')
    
print('Enjoyed this project? Well thanks! Follow me on GitHub Link: [https://github.com/pythonprogrammerandjs] Thanks!')
