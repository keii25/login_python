import login
import getpass

print("\n")
print('Registro de Nuevo Usuario....\n')

#Ingresar Nuevo Usuario
insert_user = input('Usuario: ')
insert_pass = int(getpass.getpass(prompt='Password: '))

login.database[insert_user]=insert_pass
print("\n")

print('Login.......')
print("\n")

print(login.login_acces())


