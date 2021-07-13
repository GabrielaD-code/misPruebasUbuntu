# Clase 13:  Conversor
""" pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar=3875
dolares = round(pesos / valor_dolar,2)
dolares = str(dolares)
print("Tienes $ " + dolares + " dólares")
 """
#Clase 14: Condicional
""" 
edad = int(input("¿Cuál es tu edad?: "))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
 
 #Otro ejercicio

numero = int (input("Escribe un número: "))
if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")
 """

# #Clase 15: Varios países a mi conversor de monedas
# menu= """
# Bienvenid al conversor de monedas
# :O

# 1. Pesos colombianos
# 2. Pesos argentinos
# 3. Pesos mexicanos

# Elige una opción:
# """
# opcion = int(input(menu))
# if opcion == 1:
#     pesos = input("¿Cuántos pesos colombianos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar=3875
#     dolares = round(pesos / valor_dolar,2)
#     dolares = str(dolares)
#     print("Tienes $ " + dolares + " dólares")
# elif opcion == 2:
#     pesos = input("¿Cuántos pesos argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar=65
#     dolares = round(pesos / valor_dolar,2)
#     dolares = str(dolares)
#     print("Tienes $ " + dolares + " dólares")
# elif opcion == 3:
#     pesos = input("¿Cuántos pesos mexicanos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar=20
#     dolares = round(pesos / valor_dolar,2)
#     dolares = str(dolares)
#     print("Tienes $ " + dolares + " dólares") 
# else:
#     print("Ingresa una opción correcta por favor")

# #Clase 16: Aprendiendo a no repetir código con funciones
# def imprimir_mensaje():
#     print("Mensaje especial")
#     print("Aprendiendo funciones")

# imprimir_mensaje()

# def converersacion(opcion):
#     print('Hola')
#     print('¿Cómo estás?')
#     print('Elegiste la opción '+ str(opcion))
#     print('Adios')

# opcion = int(input('Elige una opción (1 ,2 o 3): '))
# if opcion == 1:
#     converersacion(1)
# elif opcion == 2:
#     converersacion(2)
# elif opcion == 3:
#     converersacion(3)
# else:
#     print("Elige una opción correcta")

#Clase 17: Modularizando nuestro conversosr de monedas
#Uso del "return"
#def suma(a,b):
#    print('Se suman dos números')
#    resultado= a + b
#    return resultado
#
#sumatoria = suma(1,4)
#print(sumatoria)
#
#def conversor(tipo_peso, valor_dolar):
#    pesos = input("¿Cuántos pesos "+ tipo_peso +" tienes?: ")
#    dolares = round(float(pesos) / valor_dolar,2)
#    dolares = str(dolares)
#    print("Tienes $ " + dolares + " dólares")
#
#menu= """Bienvenido al conversor de monedas
#:O
#1. Pesos colombianos
#2. Pesos argentinos
#3. Pesos mexicanos
#
#Elige una opción:
#"""
#opcion = int(input(menu))
#if opcion == 1:
#    conversor("colombianos", 3875)
#elif opcion == 2:
#    conversor("argentinos", 65)
#elif opcion == 3:
#    conversor("mexicanos", 20) 
#else:
#    print("Ingresa una opción correcta por favor")

#Clase 18: Trabajando con texto: cadenas de caracteres
#nombre = ' gabriela   '
#print(nombre)
#print(nombre.strip().capitalize())
#print(nombre +' '+nombre.upper() +' '+ nombre.lower()+ ' ' + nombre[2])
#print(nombre + ' ' + nombre.replace('a','u.u'))


#Clase 19: Trabaja con textos: slices o rebanadas
#nombre = 'Gabriela'
#print('Nombre: ' + nombre)
#print('nombre[0]: ' + nombre[0] + ' nombre[1]: ' + nombre[1] + ' nombre[4]: ' + nombre[4])
#print('SLICE nombre[0:3]: ' + nombre[0:3] + ' ó lo mismo: nombre[:3]: ' + nombre[:3])
#print('SLICE nombre[3:]: ' + nombre[3:])
#print('SLICE nombre[1:8]: ' + nombre[1:8])
#print('SLICE nombre[1:8:2]: ' + nombre[1:8:2] +' 1,8 es del índice 1 al 8 y el 2 es un intervalo')
#print('SLICE nombre[::]' + nombre[::] + ' es que me lo muestre todo')
#print('SLICE nombre[1::3]: ' + nombre[1::3] + ' es que lo recorra del 1 al final pero que me muestre de intervalos de 3 y toma desde el 1')
#print('SLICE Ojo aquí nombre[::-1]: ' + nombre[::-1] + ' lo recorre todo desde el final')

#Clase 20: Proyecto: Palíndromo
#Siempre ponermos las funciones hasta arriba
#Siempre dejamos 2 líneas de espacio entre bloques
#def palindromo(palabra):
#    palabra = palabra.replace(' ','')
#    palabra = palabra.lower()
#    palabra_invertida = palabra[::-1]
#    if palabra == palabra_invertida:
#        return True
#    else:
#        return False


#--Normalmente usamos -- run() -- es estandar como main()
#def run():
#    palabra = input('Escribe una palabra para saber si es palíndormo: ')
#    es_palindromo = palindromo(palabra)
#    if es_palindromo == True:
#        print('Es palíndromo...:D')
#    else:
#        print('No es palíndromo...:C')


#Ojo aquí.... Siempre lo vamos a poner...es estandar
#-- Entri point--
#if __name__ == '__main__':
#    run()

#Clase 21: El ciclo while
#def run():
#    LIMITE = 10000
#    contador = 0
#    potencia_2 = 2**contador
#
#    while potencia_2 < LIMITE:
#        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
#        contador = contador + 1
#        potencia_2 = 2**contador
#
#
#if __name__ == '__main__':
#    run()

#Clase 23: Explorando un bucle diferente: for
#Si usamos while...Ojo que equí el contador empieza en 1 y lo imprimo antes de entrar a while por la condición que he colocado
#contador = 1
#print(contador)
#while contador < 10:
#    contador += 1
#    print(contador)

#Ojo...Se puede convertir de un RANGO a una LISTA
#a = range(100)
#print(a)
#print(list(a))

#en el ciclo for-in yo le digo que haga un ciclo que va a ir desde el 0 hasta uno antes de 1000
#for contador in range(1000):
#    print(contador)
#para la varieble contador en el rango que va de 0 al 1000(colocamos 1001 porque toma uno menos), la varieble contador irá tomando los valores del índice dentro del rango que toca e imprimiéndolo
#for contador in range(1, 1001):
#    print(contador)

#Clase 24: Rescorrer un string con un for
#def run():
#    nombre = input('Escribe tu nombre: ')
#    for letra in nombre:
#        print(letra)
#
#if __name__ == '__main__':
#    run()

#Clase 25: Interrumpiendo ciclos con break y continue
#...usando continue..cortaamos ehí ese cilo y continuemos con el siguirnte
#def run():
#    for contador in range(10):
#        #Ojo los impares no los imprime
#        if contador % 2 != 0:
#            continue
#        print(contador)
#
#if __name__ == '__main__':
#    run()

#...usando break.. termina ahí el for
#def run():
#    for i in range(10):
#        print(i)
#        if i == 7:
#            break
#
#
#if __name__ == '__main__':
#    run()

#...usando break.. termina ahí el for
#def run():
#    texto = input('Escribe un texto: ')
#    for letra in texto:
#        if letra == 'o':
#            break
#        print(letra)
#    
#
#if __name__ == '__main__':
#    run()

#Clase 26: Proyecto: prueba de primalidad
#..Números primos: sólo divisibles entre si mismos y 1
#def es_primo(numero):
#    contador = 0
#
#    for i in range(1, numero + 1):
#        if i == 1 or i == numero:
#            continue
#        if numero % i == 0:
#            contador += 1
#    if contador == 0:
#        return True
#    else: 
#        return False
#
#
#def run():
#    numero = int(input('Escribe un número: '))
#    if es_primo(numero):
#        print('Es primo')
#    else:
#        print('No es primo')
#
#
#if __name__ == '__main__':
#    run()

#Clase 27:Proyecto: videojuego Adivina el número 
#import random
#
#def run():
#    numero_aleatorio = random.randint(1,100)
#    numero_elegido = int(input('Elige un número entre 1 y 100:'))
#    while numero_elegido != numero_aleatorio:
#        if numero_elegido < numero_aleatorio:
#            print('Es más grande')
#        else:
#            print('Es más chico')
#        numero_elegido = int(input('Elige otro número: '))
#    print('¡Ganaste!')
#
#
#if __name__ == '__main__':
#    run()

#Clase 30: Qué son los diccionarios
#def run():
#    mi_diccionario = {
#        'llave1' : 1,
#        'llave2' : 2,
#        'llave3' : 3
#    }
#
#    poblacion_paises = {
#        'Argentina' : 44938712,
#        'Brasil' : 210147125,
#        'Colombia' : 50372424
#    }
#
#    print(mi_diccionario['llave2'])
#    print(' ')
#    for mivalor in mi_diccionario.values():
#        print(mivalor)
#    print(' ')
#    for llave in mi_diccionario.keys():
#        print(llave)
#    print(' ')
#    for millave, numero in mi_diccionario.items():
#        print(millave + ' su valor es: ' + str(numero))
#    print(' ')
#    for pais, poblacion in poblacion_paises.items():
#        print(pais + ' tiene: ' + str(poblacion) + ' habitantes')
#
#
#if __name__ == '__main__':
#    run()

#Clase 31: proyecto: generador:contrasena.py
#import random
#
#def generar_contrasena():
#    MAYUSCULAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
#    MINUSCULAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
#    NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
#
#    caracteres = MAYUSCULAS + MINUSCULAS + NUMEROS + CHARS
#
#    contrasena = []
#
#    for i in range(15):
#        caracter_random = random.choice(caracteres)
#        contrasena.append(caracter_random)
#    #ahora mi contraseña es una lista... pero yo la quiero string
#    contrasena = ''.join(contrasena)
#    return contrasena
#
#def run():
#    contrasena = generar_contrasena()
#    print('Tu nueva contraseña es : '+ contrasena)
#
#
#if __name__ == '__main__':
#    run()

#otra forma es 
import random
import string


def gen_pass():
    password = []
    list_char = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

    while len(password) < 16:
        chars = random.choice(list_char)
        password.append(chars)
    password = ''.join(password)
    return password


def run():
    password = gen_pass()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()