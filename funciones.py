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

#Opcion 1 MODIFICADO
def ultimasDiezPeliculas():
    contador = 0
    system("cls")
    peliculasData = requests.get('http://127.0.0.1:5000/ultimasdiezpeliculas')
    peliculas = peliculasData.json()
    # for pelicula in reversed(peliculas):
    for pelicula in peliculas:
        directorData = requests.get(f'http://127.0.0.1:5000/directores/{pelicula["idDirector"]}')
        director = directorData.json()
        generoData = requests.get(f'http://127.0.0.1:5000/generos/{pelicula["idGenero"]}')
        genero = generoData.json()
        print(f'ID {pelicula["id"]} = La pelicula "{pelicula["titulo"]}" salio en el año {pelicula["ano"]}, \
el director fue {director["nombre"]}, el genero es {genero["nombre"]}, \
la sinopsis es "{pelicula["sinopsis"]}" y la imagen es {pelicula["imagen"]}\n')
    input('Ingrese enter para continuar...')

#Opcion 2 MODIFICADO
def agregarPelicula():
    system ("cls")
    print('=====================')
    print("Registrar pelicula")
    print('=====================')
    titulo=input("Ingrese titulo: ")
    while (titulo == ""):
        system ("cls")
        print('=====================')
        print("El titulo no puede estar vacío.")
        print('=====================')
        titulo=input("Ingrese titulo: ")
    system("cls")
    ano=input("Ingrese año de la pelicula: ")
    while (len(ano) != 4):
        system("cls")
        print("=====================")
        print(ano, "no es un año valido.")
        print("=====================")
        ano=input("Ingrese año de la pelicula: ")
    idDirector=menuDirectores()
    idGenero=menuGeneros()
    system("cls")
    sinopsis=input("Ingrese sinopsis: ")
    while (sinopsis == ""):
        system ("cls")
        print('=====================')
        print("la sinopsis no puede estar vacía.")
        print('=====================')
        sinopsis=input("Ingrese sinopsis: ")
    system("cls")
    imagen=input("Ingrese URL imagen: ")
    nuevaPelicula={"id":"","titulo":titulo, "ano":ano, "idDirector":idDirector, "idGenero":idGenero, "sinopsis":sinopsis, "imagen":imagen, "idComentarios":[]}
    datos = requests.post('http://127.0.0.1:5000/peliculas/create', json=nuevaPelicula)
    mensaje = datos.text
    print("=====================")
    print(mensaje)
    print("=====================")
    input('Enter para continuar...')

#Opcion 3
def modificarPelicula():
    
    opcion = 0
    encontrada = False

    peliculaNuevaDiccionario = {"id":"","titulo":"","ano":"","idDirector":"","idGenero":"","sinopsis":"","imagen":"no cargado"}

    system('cls') 
    print('=====================')
    print('Modificar una pelicula')
    print('=====================')
    
    modificar = input('Ingrese id: ')
    peliculaData = requests.get('http://127.0.0.1:5000/peliculas')
    peliculas = peliculaData.json()
    for pelicula in peliculas:
        if pelicula["id"] == modificar:
            encontrada = True
            while opcion != 7:
                opcion = menuModificar()
                peliculaNuevaDiccionario = {"id":"","titulo":"","ano":"","idDirector":"","idGenero":"","sinopsis":"","imagen":"no cargado"}
                if opcion == 1:
                    while True:
                        valor = input(f"El titulo actualmente es '{pelicula['titulo']}', Cual es el titulo modificado?:")
                        if valor != '':
                            peliculaNuevaDiccionario['titulo'] = valor
                            break
                        else:
                            print('Error, ponga minimo una letra')
                elif opcion == 2:
                    while True:
                        valor = input(f"El ano es '{pelicula['ano']}', Cual es el ano modificado?:")
                        if len(valor) == 4:
                            peliculaNuevaDiccionario['ano'] = valor
                            break
                        else:
                            print('Error, ingrese un ano de cuatro cifras')
                elif opcion == 3:
                    peliculaNuevaDiccionario['idDirector'] = menuDirectores(pelicula['idDirector'])
                elif opcion == 4:
                    peliculaNuevaDiccionario['idGenero'] = menuGeneros(pelicula['idGenero'])
                elif opcion == 5:
                    while True:
                        valor = input(f"La sinopsis es '{pelicula['sinopsis']}', Cual es la sinopsis modificada?:")
                        if valor != '':
                            peliculaNuevaDiccionario['sinopsis'] = valor
                            break
                        else:
                            print('Error, ponga minimo una letra')
                elif opcion == 6:
                    while True:
                        valor= input(f"El imagen es '{pelicula['imagen']}', Cual es la imagen modificada?:")
                        peliculaNuevaDiccionario['imagen']  = valor

                elif opcion == 7:
                    print("=====================")
                    print('Usted esta saliendo del menu de modificacion')
                    print("=====================")
                    break
                if opcion >= 1 and opcion <=6:
                    peliculaNuevaDiccionario["id"] = modificar
                    datos = requests.put(f'http://127.0.0.1:5000/peliculas/save/', json=peliculaNuevaDiccionario)
                    mensaje = datos.text
                    print("=====================")
                    print(mensaje)
                    print("=====================")
                    input('Enter para continuar...')
    
    if encontrada == False:
        system("cls")
        print("===================================================")
        print('No existe una pelicula con esa ID')
        print("===================================================")
        input('Ingrese enter para continuar...')

#Opcion 4 MODIFICADO
def borrarPelicula(idUsuario):
    system("cls")
    print('=====================')
    print('Borrar una pelicula')
    print('=====================')
    borrar = input('Ingrese el id(0 para salir): ')
    if borrar != '0':
        datos = requests.delete(f'http://127.0.0.1:5000/peliculas/delete/{borrar}/idUsuario/{idUsuario}')
        mensaje = datos.text
        print("=====================")
        print(mensaje)
        print("=====================")
    else:
        system("cls")
        print("===================================================")
        print('Usted cancelo la eliminacion')
        print("===================================================")
    input('Ingrese enter para continuar...')

#Opcion 5 MODIFICADO
def getPeliculaByCodigo():
    system("cls")
    encontrada = False
    buscar = input('Ingrese id: ')
    peliculaData = requests.get('http://127.0.0.1:5000/peliculas')
    peliculas = peliculaData.json()
    for pelicula in peliculas:
        if pelicula['id'] == buscar:
            peliculaBuscada = pelicula
            encontrada = True
            break
        if encontrada == True:
            break
    if encontrada == True:
        directorData = requests.get(f'http://127.0.0.1:5000/directores/{pelicula["idDirector"]}')
        director = directorData.json()
        generoData = requests.get(f'http://127.0.0.1:5000/generos/{pelicula["idGenero"]}')
        genero = generoData.json()

        print(f'ID {peliculaBuscada["id"]} = La pelicula "{peliculaBuscada["titulo"]}" salio en el año {peliculaBuscada["ano"]}, \
el director fue {director["nombre"]}, el genero es {genero["nombre"]}\
, la sinopsis es "{pelicula["sinopsis"]}" y la imagen es {peliculaBuscada["imagen"]}\n')
        contador = 0

        print("=====================")
        print('COMENTARIOS')
        print("=====================")
        if peliculaBuscada['idComentarios'] != []:
            for comentarioActual in peliculaBuscada['idComentarios']:
                comentarioData = requests.get(f'http://127.0.0.1:5000/comentario/{comentarioActual}')
                comentario = comentarioData.json()
                contador = contador + 1
                print(f'{contador}) {comentario["comentario"]}')
            print('')
        else:
            print('Esta pelicula no tiene comentarios\n')
    else:
        print("=====================")
        print('Error al buscar comentario, no encontrado')
        print("=====================")
    input('Ingrese enter para continuar...')
