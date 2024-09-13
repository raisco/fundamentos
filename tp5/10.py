#  Un complejo de cines necesita un programa para contabilizar el dinero que re
# cauda. Por cada función se ingresa la cantidad de espectadores y si esa función 
# tiene descuento o no (1=Sí, 2=No). La carga finaliza cuando la cantidad de es
# pectadores sea igual a cero.  En ese momento el programa deberá:
#  · Calcular la recaudación total del complejo, considerando que el valor de la 
# entrada es de $3500 en los días de descuento $5000 en los días sin 
# descuento.
#  · Determinar cuántos espectadores ingresaron con descuento y qué 
# porcentaje representan sobre el total de funciones
recaudacion_total = 0  
espectadores_con_descuento = 0  
total_espectadores = 0   
cantidad_espectadores = -1   
while cantidad_espectadores != 0:    
    cantidad_espectadores = int(input("Ingrese la cantidad de espectadores (0 para terminar): "))  
    if cantidad_espectadores > 0:   
        descuento = int(input("¿La función tiene descuento? (1=Sí, 2=No): "))  
        if descuento == 1:  
            recaudacion_total += cantidad_espectadores * 3500   
            espectadores_con_descuento += cantidad_espectadores  
        elif descuento == 2:  
            recaudacion_total += cantidad_espectadores * 5000 
        total_espectadores += cantidad_espectadores  
if total_espectadores > 0:  
    porcentaje_descuento = (espectadores_con_descuento / total_espectadores) * 100  
else:  
    porcentaje_descuento = 0  
 
print("Recaudación total: $", recaudacion_total)  
print("Total de espectadores con descuento: ", espectadores_con_descuento)  
print("Porcentaje de espectadores con descuento: ", porcentaje_descuento)
