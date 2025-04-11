import os
import time

def generarTrianguloPascal(n):
    triangulo = []
    for i in range(n + 1):
        fila = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        triangulo.append(fila)
    return triangulo

def mostrarPolinomio(coeficientes):
    terminos = []
    grado = len(coeficientes) - 1
    for i, coef in enumerate(coeficientes):
        grado_actual = grado - i
        if coef == 0:
            continue
        if grado_actual == 0:
            terminos.append(str(coef))
        else:
            termino = f"{coef if coef != 1 else ''}x"
            if grado_actual > 1:
                termino += f"^{grado_actual}"
            terminos.append(termino)
    return " + ".join(terminos)

def expandirPolinomio(n):
    print(f"\nExpandiendo (x + 1)^{n} usando el Triángulo de Pascal:\n")
    
    # Generar el triángulo de Pascal hasta el nivel n
    triangulo = generarTrianguloPascal(n)
    
    # Mostrar el triángulo de Pascal generado
    print("Triángulo de Pascal generado:")
    for i, fila in enumerate(triangulo):
        print(f"n={i}: {fila}")
        time.sleep(2)
    
    # Obtener los coeficientes para (x + 1)^n
    coeficientes = triangulo[n]
    
    # Mostrar los coeficientes encontrados
    print(f"\nCoeficientes para (x + 1)^{n}= {coeficientes}")
    
    # Mostrar el polinomio expandido
    polinomio = mostrarPolinomio(coeficientes)
    print(f"\nPolinomio expandido:")
    print(f"(x + 1)^{n} = {polinomio}\n\n")



def obtenerPolinomio():
    try:
        n = int(input("\nIngrese el exponente n: "))
        if n < 0:
            print("Por favor ingrese un número entero no negativo.")
            os.system('pause')
        else:
            expandirPolinomio(n)
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")
        os.system('pause')
    
    

salir = False
opcion = 0
while(salir != True):
    os.system('cls')
    print("Obtener polinomio de un (x+1)^n")
    print("[1]. Evaluar [2]. Salir")
    try:
        opcion = int(input("Ingrese la opcion: "))
    except:
        print("Opcion ingresada es invalida")
        os.system('pause')

    if(opcion == 1):
        obtenerPolinomio()
        os.system('pause')
    elif (opcion == 2):
        salir = True

    
    
