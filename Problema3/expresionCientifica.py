import re
import ast
import os

def evaluarExpresion(expresion):
    # Reemplazar la notación científica (Ej: 125E10 -> 125e10)
    expresion = re.sub(r'(\d+\.?\d*)E([+-]?\d+)', r'\1e\2', expresion, flags=re.IGNORECASE)
    
    try:
        
        tree = ast.parse(expresion, mode='eval')
        '''
            Convierte la expresión de texto en un Árbol de Sintaxis Abstracta
            Python analiza la cadena de texto (expresion)
            Crea una estructura de árbol con nodos que representan: Numero, operadores, parentesis
        '''
        # Verificar que solo contenga operaciones matemáticas permitidas
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                raise ValueError("Llamadas a funciones no permitidas")
            if isinstance(node, ast.Name):
                raise ValueError("Variables no permitidas")
        
        resultado = eval(compile(tree, filename='<string>', mode='eval'))
        
        '''
            compile Compila el AST en bytecode de Python (código intermedio que la máquina virtual de Python puede ejecutar)
            eval Ejecuta el bytecode compilado y devuelve el resultado numérico de la expresión
        '''

        return resultado
    except (SyntaxError, ValueError, ZeroDivisionError) as e:
        return f"Error: {str(e)}"


salir = False
opcion = 0
while(salir != True):
    os.system('cls')
    print("Evaluar expresion matematica y cientifica")
    print("[1]. Evaluar [2]. Salir")
    try:
        opcion = int(input("Ingrese la opcion: "))
    except:
        print("Opcion ingresada es invalida")
        os.system('pause')
    
    if (opcion == 1 ):
        os.system('cls')
        expresionMatematica = str(input("Ingrese la expresion a evaluar: ")) 
        result = evaluarExpresion(expresionMatematica)
        if(type(result) != str):
            print(f"El resultado para la expresion ingresada {expresionMatematica} es: {result}")
        else:
            print(result)
        os.system('pause')
    elif (opcion == 2):
        salir= True



'''
        Ejemplo
    (125E10-1E15)/5E-85*15

'''
