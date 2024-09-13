# Ingresar un número N y validar que sea positivo. Luego:
#  a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
#  b. Informar la suma de esos números impares.
#  Ejemplo:
#  Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
#  Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
#  Si se ingresa -5, se debe pedir otro número.
N = -1   
while N <= 0:  
    N = int(input("Ingrese un número positivo: "))  
    if N <= 0:  
        print("Por favor, ingrese un número positivo.")  
num = 1  
suma_impares = 0  
print("Los números impares son:")  
while num <= N:  
    print(num) 
    suma_impares += num  
    num += 2    
print("La suma de los números impares es:", suma_impares)   