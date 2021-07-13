import random

is_game = True

def conversacion(mensaje):
  if mensaje == 'piedra':
    return 1
  elif mensaje == 'papel':
    return 2
  elif mensaje == 'tijera':
    return 3
  else:
    return 0

def quien_gano(oponente, ususario):
  if (oponente == 1 and usuario == 2) or (oponente == 3 and usuario == 1) or (oponente == 2 and usuario == 3):
    return 'GANASTEEEEE UJUUU🎉🎉'
  elif( oponente == 2 and usuario == 1) or (oponente == 1 and usuario == 3) or (oponente == 3 and usuario == 1):
    return 'No, ya perdiste :C'
  elif oponente == usuario:
    return 'lol fue un empate'
  elif oponente == 0 or usuario == 0:
    return 'Error ocurrió algo extraño ???????'
  else:
    return 'Error???????'

def seguir_jugando(respuesta):
  if respuesta == 'si' or respuesta == 's':
    return True
  else:
    return False


bienvenida = """ 
B I E N V E N I D O . . . 


    AQUÍ SE DESAFÍA...

                  AQUÍ HAY SANGRE...

        LA MUERTE ES INEVITABLE...


     ¿ ESTÁS PREPARADO ?

                ENTONCES...


          B I E N V E N I D O... 
                  A . . . 

██████╗ ██╗███████╗██████╗ ██████╗  █████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║█████╗  ██║  ██║██████╔╝███████║
██╔═══╝ ██║██╔══╝  ██║  ██║██╔══██╗██╔══██║
██║     ██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

  ██████╗  █████╗ ██████╗ ███████╗██╗     
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     
  ██████╔╝███████║██████╔╝█████╗  ██║     
  ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██║     
  ██║     ██║  ██║██║     ███████╗███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝

                   ██████╗ 
                  ██╔═══██╗
                  ██║   ██║
                  ██║   ██║
                  ╚██████╔╝

████████╗██╗     ██╗███████╗██████╗  █████╗ 
╚══██╔══╝██║     ██║██╔════╝██╔══██╗██╔══██╗
   ██║   ██║     ██║█████╗  ██████╔╝███████║
   ██║   ██║██   ██║██╔══╝  ██╔══██╗██╔══██║
   ██║   ██║╚█████╔╝███████╗██║  ██║██║  ██║
   ╚═╝   ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
________________________________________________

            -= PRESIONE START =-

"""

print(bienvenida)

while is_game:
  oponente = random.randint(1,3)
  usuario = conversacion(input('¿Cuál eliges Piedra, papel o tijera?...'))
  
  print("oponente: " +str(oponente)+ " Usuario: " +str(usuario))
  print(quien_gano(oponente, usuario))
  is_game = seguir_jugando(input('¿Quieres seguir jugando? (s/n) '))   

  #Para el text utilicé un generador de arte de ASCII más específico el ANSI Shadow de https://patorjk.com/software/taag/#f=ANSI Shadow