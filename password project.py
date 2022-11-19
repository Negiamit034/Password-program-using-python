user_name=input('User Name:')
password=input('Pasword:')
password_length=len(password)
password_code='*'*password_length
print(f'hello {user_name},your password is {password_code},and is {password_length} letters long')