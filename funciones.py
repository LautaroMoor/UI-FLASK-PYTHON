from os import system
import requests

#MENU PRINCIPAL
def MenuBienvenida():
    opcion = 0
    while not(opcion>=1 and opcion<=3):
        system("cls")
        print('=====================')
        print('\tBienvenido')
        print('=====================')
        print('1) Iniciar sesion')
        print('2) Ingresar como invitado')
        print('3) Para salir')
        print('=====================')
        opcion = int(input('Ingresar opcion: '))
    return opcion

#LOGEO USUARIO
def opcionIniciarSesion():
    system("cls")
    exitoso = False
    while True:
        system('cls')
        print('=====================')
        print('Inicio sesion usuarios')
        print('=====================')
        while True:
            usuarioIngresado = input('Ingrese su usuario: ').lower()
            contrasenaIngresada =  input('Ingrese su contrasena: ').lower()
            if usuarioIngresado == '' or contrasenaIngresada == '':
                print ('No puede dejar los campos vacios')
                input('Enter para continuar...')
                system('cls')
                continue
            break
        print('=====================')
        check = requests.get(f'http://127.0.0.1:5000/usuario/{usuarioIngresado}/contrasena/{contrasenaIngresada}')
        id = check.text
        system('cls')
        if id == 'Error' or id == None:
            print("=====================")
            print('Usuario y/o contrasena incorrecta')
            print("=====================")
            input('Enter para continuar...')
            continue
        else:
            print("=====================")
            print('Logeo exitoso')
            print("=====================")
            input('Enter para continuar...')
            return id

#MENU USUARIO LOGEADO
def menuUsuario():
    opcion = 0
    while not(opcion>=1 and opcion<=13):
        system("cls")
        print('=====================')
        print('\tMenu principal')
        print('=====================')
        print('1) Ver ultimas 10 peliculas agregadas')
        print('2) Agregar pelicula')
        print('3) Modificar pelicula')
        print('4) Borrar pelicula')
        print('5) Buscar pelicula por ID')
        print('6) Mostrar todas las peliculas')
        print('7) Mostrar directores')
        print('8) Mostrar generos')
        print('9) Mostrar peliculas que tengan portada')
        print('10) Mostrar peliculas por director')
        print('11) Comentarios')
        print('=+=+=SORPRENDEME=+=+=')
        print('12) Mostar una pelicula random del catalogo')
        print('=+=+=+=+=+=+=+=+=+=+=')
        print('13) Salir/Deslogear')
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion
