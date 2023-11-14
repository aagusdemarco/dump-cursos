# Ejercicio 1

comidas = ['empanadas', 'asado', 'medialunas', 'tarta', 'milanesas']
nombre_archivo = 'comidas.txt'

with open(nombre_archivo, 'w') as archivo:
    for comida in comidas:
        archivo.write(comida + '\n')
    

# Ejercicio 2

with open('AP\modulo9\credenciales.txt', 'r') as credencial:
    lineas = credencial.readlines()

print(lineas)
mail = lineas[0].strip()
password = lineas[1].strip()
print(mail)
print(password)