# Ejercicio 1

nombreUsuario = input('Ingrese su nombre: ')
apellidoUsuario = input('Ingrese su apellido: ')

def saludoA(nombre, apellido):
    saludo = f'Hola {nombre} {apellido}, sea bienvenido.'
    return saludo

print(saludoA(nombreUsuario, apellidoUsuario))


# Ejercicio 2

password = input('Ingrese su contraseña: ')

def seguridad(contrasenia):
    esSegura = False
    esLarga = False
    tieneNumero = False

    if len(contrasenia) >= 8:
        esLarga = True

    for i in range(len(contrasenia)):
        if contrasenia[i].isnumeric():
            tieneNumero = True
    
    if esLarga and tieneNumero:
        esSegura = True
    else: esSegura = False

    return esSegura

print(seguridad(password))


# Ejercicio 2

def mi_funcion():
    print("Entra en mi_funcion")
    return
    print("No llega")
mi_funcion() # Entra en mi_funcion

def saludo(nombre):
    return "Hola " + nombre

bienvenida = saludo("Martina")
print(bienvenida)


# Ejercicio 3

password2 = input('Ingrese su contraseña: ')

def errorContrasenia(contrasenia):
    hayError = False
    largoProhibido = False
    letrasProhibidas = False

    for i in range(len(contrasenia)):
        if contrasenia[i] == 'ñ' or ' ':
            letrasProhibidas = True

    if len(contrasenia) > 8 or len(contrasenia) < 4:
        largoProhibido = True

    if largoProhibido and letrasProhibidas:
        hayError = True
    else: hayError = False

    return hayError

print(errorContrasenia(password2))

num = input('Ingrese un numero: ')

def compruebaNum(numero):
    cumpleRequisitos = False
    mayorQueN1 = False
    menor9digitos = False
    if int(numero) > 20000000:
        mayorQueN1 = True

    if len(numero) < 9:
        menor9digitos = True

    if menor9digitos and mayorQueN1:
        cumpleRequisitos = True

    return cumpleRequisitos

print(compruebaNum(num))


# Ejercicio 4

def funcion():
    nombres = input('Ingrese los nombres que deseas convertir separados por una coma: ')
    listaNombres = list(nombres.split(','))
    
    listaCapitalizados = []

    for name in listaNombres:
        name = name.capitalize()
        listaCapitalizados.append(name)
    
    print('Los nombres convertidos son: ')
    return listaCapitalizados

print(funcion())


# Ejercicio 5

variableASeguir = "micontrasenia"
entrada = input("ingrese la contraseña: ")
if entrada.lower() == variableASeguir:
  print("todo ok")
else:
  print("Todo mal")


# Desafio 4

def gestorTareas(listaTareas):
    crearTarea = listaTareas.append(input('Ingrese una tarea: '))
    print(f'La tarea {crearTarea} fue agregada a la lista.')
    print(listaTareas)

    borrarTarea = listaTareas.remove(input('Ingrese la tarea a borrar: '))
    print(f'La tarea {borrarTarea} fue borrada de la lista')
    print(listaTareas)

    indice = listaTareas.index(input('Ingrese tarea a modificar: '))
    listaTareas[indice] = input('Ingrese tarea modificada: ')
    print(f'La tarea fue modificada')

    return listaTareas

print(gestorTareas(['compras', 'trabajar', 'limpiar', 'ordenar']))
