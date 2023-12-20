user={'username':'abc','passwoard':'12345'}
username=input('enter the user name:-')
passwoard=input('enter the passwoard:-')
if username==user['username'] and passwoard==user['passwoard']:
    print('hello abc')
else:
    print('user not exist')
