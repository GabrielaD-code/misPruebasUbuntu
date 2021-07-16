def run():
    maximo = int(input('Elige un valor entero: '))
    i = maximo
    contador = 0
    while i > 0:
        imprimir = '*' * i
        print(imprimir + ' ' * contador + imprimir)
        i -= 1
        contador += 2
    contador -= 2
    i = 1
    
    while i < maximo + 1:
        imprimir = '*' * i
        print(imprimir + ' ' * contador + imprimir)
        i += 1
        contador -= 2


if __name__ == '__main__':
    run() 