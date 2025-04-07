a= input('username: ')
b= input('password: ')
if not bool(a.strip()) and not bool(b.strip()):
    print("You did not enter username or password. Please enter them: ")
else:
    print('you entered: ', a, b)