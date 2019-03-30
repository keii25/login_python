import getpass
#import crypt
import datos

# Datos de entrada
database = {}

def login_acces():
    i = 0
    while i < 3:
        insert_user = input('Usuario: ')
        insert_pass = int(getpass.getpass(prompt='Password: '))  
        password = crypt.crypt(str(insert_pass), 'salt')     
        print("\n")
        if insert_user in database and insert_pass == database[insert_user]:
            return datos.acciones()
            break
        else:
            print("Acceso Denegado..Vuelva a intentarlo\n")           
        i+=1
    if i ==3:
        print("Has sobrepasado el numero de intentos...")
        



    
     









