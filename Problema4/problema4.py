import os

def contarPalabra(cadena, palabraBuscar):
    # Convertir la cadena y la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
    cadenaMinus = cadena.lower()
    palabraMinus = palabraBuscar.lower()
    
    # Contar ocurrencias
    ocurrencias = cadenaMinus.count(palabraMinus)
    
    # Mostrar todas las ocurrencias con su posición
    print(f"\nCadena analizada: '{cadena}'")
    print(f"Buscando la palabra: '{palabraBuscar}'")
    print(f"\nTotal de ocurrencias encontradas: {ocurrencias}")
    
    if ocurrencias > 0:
        print("\nPosiciones donde aparece:")
        indice = 0
        while indice < len(cadena):
            indice = cadenaMinus.find(palabraMinus, indice)
            if indice == -1:
                break
            print(f"- Posición {indice}: '{cadena[indice:indice+len(palabraBuscar)]}'")
            indice += len(palabraBuscar)
        print("\n\n")

salir = False
opcion = 0
while(salir != True):
    os.system('cls')
    print("Encontrar palabras en cadenas de lenguaje Python o texto")
    print("[1]. Buscar [2]. Salir")
    try:
        opcion = int(input("Ingrese la opcion: "))
    except:
        print("Opcion ingresada es invalida")
        os.system('pause')
    
    if(opcion == 1):
        entrada = input("Ingrese la cadena codigo python o texto: ")
        palabra = input("Ingrese la palabra a buscar: ")
        contarPalabra(entrada, palabra)
        os.system('pause')
    elif(opcion == 2):
        salir = True


'''
            Ejemplo
        print("Cadena analizada: '{cadena}'") input("Ingrese la cadena de texto (código Python o texto): ")
'''