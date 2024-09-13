# Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y 
# un número entero N que representa una cantidad de días. Realizar un programa 
# que imprima la nueva fecha que resulta de sumar N días a la fecha dada. Tener 
# en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3
D=int(input('ingresar dia: '))
M=int(input('ingresar mes: '))
A=int(input('ingresar año: '))
N=int(input('agregar dias a la fecha: '))
bisiesto = (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0)
if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
    dias_mes = 31
elif M == 4 or M == 6 or M == 9 or M == 11:
    dias_mes = 30
elif M == 2:
    dias_mes = 29 if bisiesto else 28
else:
    dias_mes = 0 
D += N
while D > dias_mes:
    D -= dias_mes  
    M += 1        
    if M > 12:    
        M = 1      
        A += 1    
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        dias_mes = 31
    elif M == 4 or M == 6 or M == 9 or M == 11:
        dias_mes = 30
    elif M == 2:
        dias_mes = 29 if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0) else 28
print(D,M,A)