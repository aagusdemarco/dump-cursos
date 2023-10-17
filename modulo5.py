# Ejercicio 1

import os

directorio = os.getcwd()
print(directorio) #C:\Users\demar\OneDrive\Desktop\Codigo


# Ejercicio 2

import random

lista = []
for i in range(10):
    lista.append(random.randint(0,10))

print(lista)


# Ejercicio 3


# Ejercicio 4

#Tenemos todas las formas de importar librerías en Python.
#Descomentá la linea que hace que el código funcione

import numpy as np
# import numpy
# import numpy *
# from numpy import sum, arange, sqrt

valor = 25
raiz = np.sqrt(valor)
print(raiz)