#Ejercicio 1

# - No entendi / falta info en la consigna

#Ejercicio 2

for x, i in enumerate(range(5, 46, 5)):
    print(f'El multiplo {x + 1} de 5 es {i}')

#Ejercicio 3

num1 = 150
for num in range(1, 6):
    siguiente = num1 + num
    anterior = num1 - num
    print(anterior, siguiente)

#Ejercicio 4

for indice, mult in enumerate(range(2, 21, 2)):
    print(f'El multiplo {indice + 1} de 2 es {mult}')

#Desafio 3

marcasAutos = ['Ford', 'Chevrolet', 'Dodge', 'Volkswagen', 'Peugeot', 'Toyota', 'Fiat', 'Renault', 'Honda', 'Mercedes Benz']

for posicion, marca in enumerate(marcasAutos):
    print(f'Posición {posicion}: {marca}')