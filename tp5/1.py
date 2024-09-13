#  Leer números que representan edades de un grupo de personas, finalizando la 
# lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18 
# años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
# Descartar valores que no representan una edad válida. (Se considera válida una 
# edad entre 0 y 100)
mayores=0
menores=0
suma_menores=0
suma_mayores=0
edades=int(input('ingresar edades: '))
while edades!=-1:
    if edades<=17:
        menores+=1
        suma_menores+=edades
    elif edades>=18 and edades<=100:
        mayores+=1
        suma_mayores+=edades
    edades=int(input('ingresar edades: '))
promedio_grupo_menores=suma_menores/menores
promedio_grupo_mayores=suma_mayores/mayores      
print('los que son menores de 18 años son: ',menores,'y el promedio de edad de los mayores es: ',promedio_grupo_menores)   
print('los que son mayores son: ',mayores,' y el promedio de edad de los mayores es: ', promedio_grupo_mayores)

















