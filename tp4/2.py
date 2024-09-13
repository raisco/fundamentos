# Realizar un programa para ingresar desde el teclado un conjunto de números e 
# informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar la lectura de datos con -1. 
num=int(input('ingresar numeros'))

while  num!=-1:
    if num%2==0:
        print('el numero es par')

    else:
        print('el numero es impar')
    num=int(input('ingresar -1 para terminar'))