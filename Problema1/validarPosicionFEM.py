import re
import os

def esNotacionFEM(fen):
    # Expresión regular para validar la parte de la posición del FEN
    patronPosicion = re.compile(
        r'^\s*([rnbqkpRNBQKP1-8]+\/){7}[rnbqkpRNBQKP1-8]+\s[wb]\s(-|K?Q?k?q?)\s(-|[a-h][1-8])\s\d+\s\d+\s*$'
    )
    
    # Verificar si coincide con el patrón
    if not patronPosicion.match(fen):
        return False
    
    # Dividir el FEN en sus partes principales
    partes = fen.split()
    if len(partes) != 6:
        return False
    
    # Validar la sección del tablero
    filas = partes[0].split('/')
    if len(filas) != 8:
        return False
    
    for fila in filas:
        suma = 0
        for c in fila:
            if c.isdigit():
                suma += int(c)
            elif c.lower() in ['p', 'n', 'b', 'r', 'q', 'k']:
                suma += 1
            else:
                return False
        if suma != 8:
            return False
    
    # Validar el turno (debe ser 'w' o 'b')
    if partes[1] not in ['w', 'b']:
        return False
    
    # Validar enroques
    if partes[2] != '-' and not re.fullmatch(r'^K?Q?k?q?$', partes[2]):
        return False
    
    # Validar casilla de al paso (debe ser '-' o casilla válida)
    if partes[3] != '-':
        if not re.fullmatch(r'^[a-h][36]$', partes[3]):
            return False
    
    # Validar número de medio movimientos y número de movimientos completos
    try:
        int(partes[4])  # Medio movimientos
        int(partes[5])  # Movimientos completos
    except ValueError:
        return False
    
    return True

salir = False
opcion = 0
while(salir != True):
    os.system('cls')
    print("Validacion de notacion FEM (Forsyth-Edwards Notation)")
    print("[1]. Evaluar una cadena  [2]. Salir")
    try:
        opcion = int(input("Ingrese la opcion: "))
    except:
        print("Opcion ingresada es invalida")
        os.system('pause')
    
    if (opcion == 1 ):
        os.system('cls')
        cadenaFEM = str(input("Ingrese la cadena a evaluar: ")) 
        if (esNotacionFEM(cadenaFEM)):
            print(f"La cadena ''{cadenaFEM}''  si esta en notacion FEM")
        else:
            print(f"La cadena ''{cadenaFEM}''  no esta en notacion FEM")

        os.system('pause')
    elif (opcion == 2):
        salir= True

        

'''
                  Ejemplos

    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    8/8/8/8/8/8/8/8 w - - 0 1
    rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1
    rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 extra  
    rnbqkbnr/pppppppp/9/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR x KQkq - 0 1
        
'''