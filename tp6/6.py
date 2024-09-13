# Escribir la función comparar(a, b) que reciba como parámetros dos números en
# teros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si 
# el primero es menor que el segundo. En este ejercicio debe aprovecharse la fun
# ción del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) 
# devuelve -1.
import ej5

def comparar(a,b):
    return ej5.signo(a-b)
    


a=int(input('ingresar numero a: '))
b=int(input('ingresar numero b: '))
print(comparar(a,b))

