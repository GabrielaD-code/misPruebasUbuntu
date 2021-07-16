
#Clase 11: Representación de flotantes
#x = 0.0
#for i in range(10):
#    x += 0.1
#
#if x == 1.0:
#    print(f'x = {x}')
#else:
#    print(f'x != {x}')
#
#Nunca usar == con valores de tipo flotante porque no son exactos, siempre usar < ó >

#Clase 12: Enumeración exhaustiva
#objetivo = int(input('Elige un entero para saber si tiene raíz cuadrada: '))
#respuesta = 0
#
#while respuesta**2 < objetivo:
#    print(respuesta)
#    respuesta += 1
#
#if respuesta**2 == objetivo:
#    print(f'Laa raíz cuadrada de {objetivo}  es  {respuesta}')
#else:
#    print(f'{objetivo}  no tiene una raíz cuadrada exacta :O ')
#
#0.0--0.0--4 0.01--0.001--3.99 0.02--0.004--3.96
#clase 13: Aproximación de soluciones
#objetivo = int(input('Escoje un número: '))
#epsilon = 0.01
#paso = epsilon**2
#respuesta = 0.0
#
#while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
#    print(abs(respuesta**2 - objetivo), respuesta)
#    respuesta += paso
#
#if abs(respuesta**2 - objetivo) >= epsilon:
#    print(f'No se encontró la raíz cuadrada de {objetivo}')
#else:
#    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
#

#Clase 14: Búsquedas binarias
objetivo = int(input('Escoge un número para saber su raíz cuadrada: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0,objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo: {bajo}, alto: {alto}  respuesta: {respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2
print(f'La raíz cuadrada de {objetivo} es {respuesta}')