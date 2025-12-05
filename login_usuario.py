import csv

with open('login.csv', 'r') as log:

    log = list(csv.reader(log))

    while_main = True
    while_int = True
    
    meter = 0
    while while_main:

        while while_int:

            user = input('USUARIO: ')
            password = input('CONTRASEÑA: ')

            for line in log:
                if line[1] == user and line[2] == password:     # Comparo usuario y constraseña
                    print(f'Bienvenido {line[0]}')
                    while_int = False   # bandera para el while interno
                    break    # paro el for
            else:
                print('\nError de untentiticación, intente nuevamente')

                meter += 1  # importante sumar solo si la autentificacion falla
                if meter == 3:  # Verifico para cambiar las variables del while y acabar el codigo
                    while_int = False    # bandera interna
                    while_main = False    # bandera externa
                    print('\nUsuario bloqueado. 3 intentos fallidos')
                
        
        if meter == 3:  # Aquí verifico para omitir todo el resto de codigo y acabar todo el codigo
            continue    # esto salta el codigo de aqui en adelante, y como la bandera externa fue cambiada entonces acaba el while externo
        
        print('\nhola seguimos')  # empieza a ejecutarse el codigo fuera del while si la autentificacion fue exitosa
        break
