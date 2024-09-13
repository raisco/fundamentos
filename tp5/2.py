#      Escribir un programa que permita ingresar los números de legajo de los alumnos 
# de un curso y su nota de examen final. El fin de la carga se determina ingresan
# do un -1 en el legajo. Informar para cada alumno si aprobó o no el examen con
# siderando que se aprueba con nota mayor o igual a 4. Se debe validar que la 
# nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
#  ·
#  ·
#  ·
#  Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#  Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
#  Porcentaje de alumnos que están aplazados (tienen 1 en el examen)
cant_aprobados=0
cant_Desaprobados=0
cant_aplazados=0
numero_de_legajo=int(input('ingresar numero de legajo: '))
while numero_de_legajo!=-1:
    nota_final=int(input('ingresar nota del examen final: '))
    while nota_final<1 or nota_final>10:
        nota_final=int(input('ERROR, INGRESE UNA NOTA ENTRE 1 Y 10: '))
    if nota_final==1:
        cant_aplazados+=1
        print('APLAZADO')
    elif nota_final<4 :
        cant_Desaprobados+=1
        print('REPROBADO')
    elif nota_final>=4 and nota_final<=10:
        cant_aprobados+=1
        print('APROBADO')
    numero_de_legajo=int(input('ingresar numero de legajo: '))
total_alumnos=cant_aplazados+cant_aprobados+cant_Desaprobados
print('el porcentaje de alumnos aplazados es de ',(cant_aplazados*1/total_alumnos))
print('La cantidad de alumnos reprobados es de: ', cant_Desaprobados,'La cantidad de alumnos aprobados es de: ',cant_aprobados)

        

