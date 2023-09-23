#Ejercicio 1

num1 = 800
num2 = 545
num3 = 10
num4 = 25

sum4 = num1 + num2 + num3 + num4
dif = num1 - num2
resto = num2 % num4
potencia = num1 ** 3, num2 ** 3, num3 ** 3, num4 ** 3
cociente = num2 / num4

print(sum4)
print(dif)
print(resto)
print(potencia)
print(cociente)


#Ejercicio 2

if 3 > 2:
    print('3 es mayor que 2')

if 4 == 5:
    print('4 es igual que 5')
#solo las condiciones verdaderas se ejecutan


#Ejercicio 3

if 15 > 100:
    print('15 es mayor que 100')
else: print('15 no es mayor que 100')


#Ejercicio 4

base = int(input('ingrese la base del triangulo: '))
altura = int(input('ingrese la altura del triangulo: '))
area = base * altura

print(f'El area del triangulo cuya base es {base} y cuya altura es {altura} es de {area}')


#Ejercicio 5

edad = int(input('ingrese su edad: '))
genero = input('ingrese su genero (mujer/hombre): ')
if genero.lower() == 'mujer' and edad < 60:
    print(f'Esta en edad de jubilarse, pues es {genero} y tiene {edad} años')
elif genero.lower() == 'mujer' and edad >= 60:
    print(f'Esta en edad de jubilarse, pues es {genero} y tiene {edad} años')
elif genero.lower() == 'hombre' and edad < 65:
    print(f'Esta en edad de jubilarse, pues es {genero} y tiene {edad} años')
elif genero.lower() == 'hombre' and edad >= 65:
    print(f'Esta en edad de jubilarse, pues es {genero} y tiene {edad} años')


#Desafio 2

print('Bienvenidos a la calculadora')
print('Las operaciones son suma, resta, multi, y div')

a = int(input('ingrese un numero: '))
b = int(input('ingrese un numero: '))
operacion = input('ingrese una operacion: ')

if operacion.lower() == 'suma':
    resultado = a + b
    print(resultado)
elif operacion.lower() == 'resta':
    resultado = a - b
    print(resultado)
elif operacion.lower() == 'multi':
    resultado = a * b
    print(resultado)
elif operacion.lower() == 'div':
    resultado = a / b
    print(resultado)
else: print('Operacion Invalida')