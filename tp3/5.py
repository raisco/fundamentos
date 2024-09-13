# Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, 
# aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está 
# entre 0 y 10.
# · Se promociona cuando las notas de ambos parciales son mayores o 
# iguales a 7.
# · Se aprueba cuando las notas de ambos parciales son mayores o iguales 
# a 4.
# · Se debe recuperar cuando al menos una de las dos notas es menor a 4.
parcial_1=float(input('ingresar nota del primer parcial'))
paricial_2=float(input('ingresar nota del segundo parcial'))
promedio=(parcial_1+paricial_2)//2 
if promedio>0 and promedio <4:
  print('desaprobado,debes recuperar',promedio)
elif promedio>=4 and promedio<=6:
  print('aprobado',promedio)
elif promedio>=7 and promedio <=10:
  print('felicidades, has promocionado',promedio)

else: print('error')
