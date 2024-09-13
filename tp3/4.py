# En el congreso se vota una ley muy importante. Desarrollar un programa que 
# permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso y si la misma fue aprobada o no 
cantidad_de_votos_a_favor=int(input('ingresar votos a favor'))
cantidad_De_votos_en_contra=int(input('ingresar datos en contra'))
total=cantidad_De_votos_en_contra+cantidad_de_votos_a_favor
porcentaje_a=cantidad_de_votos_a_favor*100/ total
porcentaje_b=cantidad_De_votos_en_contra*100/total
if cantidad_de_votos_a_favor > cantidad_De_votos_en_contra:
    print('la nueva ley fue aprobada por el',porcentaje_a)
else: print('la nueva ley no fue aprobada',porcentaje_b)