#  Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el 
# número invertido. Tener en cuenta que el número puede ser negativo. Por ejem
# plo, si se ingresa 1234 debe mostrar 4321.
num=int(input('ingresar un numero: '))
i=0
while num> 0:  
    cifra = num % 10   
    i = i * 10 + cifra 
    num = num// 10
print(i)